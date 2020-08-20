from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail

from .forms import CommentForm, PostForm
from .models import Post, Category, Author
from marketing.models import Subscriber
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import random


# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
    }
    return render(request, 'search_result.html', context)


def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = False
        sub.save()
        return render(request, 'index.html', {'email': sub.email, 'action': 'deleted'})
    return redirect('/', {})


def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'index.html', {'email': sub.email, 'action': 'confirmed'})
    return render(request, 'index.html', {'email': sub.email, 'action': 'denied'})


@csrf_exempt
def index(request):
    featured_posts = Post.objects.filter(featured=True)
    latest_posts = Post.objects.order_by("-timestamp")[0:3]
    if request.method == 'POST':
        new_subscriber = Subscriber(email=request.POST["email"], confirmation_num=random_digits())
        new_subscriber.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=new_subscriber.email,
            subject='Thank you for singing up for email newsletter!',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&confirmation_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                       new_subscriber.email,
                                                       new_subscriber.confirmation_num))

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            sg.send(message)
        except Exception as e:
            print(e)

        context = {'featured_posts': featured_posts,
                   'latest_posts': latest_posts,
                   'email': new_subscriber.email,
                   'action': 'added'}
        return render(request, 'index.html', context)

    context = {'featured_posts': featured_posts,
               'latest_posts': latest_posts}
    return render(request, 'index.html', context)


def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    latest_posts = Post.objects.order_by("-timestamp")[0:3]
    category_list = Category.objects.all()
    context = {'queryset': paginated_queryset,
               'page_request_var': page_request_var,
               'latest_posts': latest_posts,
               'category_list': category_list,
               }

    return render(request, 'blog.html', context)


def post(request, pk):
    post = get_object_or_404(Post, id=pk)
    latest_posts = Post.objects.order_by("-timestamp")[:3]
    category_list = Category.objects.all()
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'pk': post.pk,
            }))
    context = {'post': post,
               'latest_posts': latest_posts,
               'category_list': category_list,
               'form': form,
               }
    return render(request, 'post.html', context)


def post_create(request):
    operation_type = 'Create'
    form = PostForm(initial={'author': get_author(request.user)})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("post-detail", kwargs={'pk': form.instance.id}))
    context = {
        'operation_type': operation_type,
        'form': form,
    }
    return render(request, "post_form.html", context)


def post_update(request, pk):
    operation_type = 'Update'
    post = get_object_or_404(Post, id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse("post-detail", kwargs={'pk': form.instance.id}))
    context = {
        'operation_type': operation_type,
        'form': form,
    }
    return render(request, 'post_form.html', context)


def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post-list')
    context = {'post': post}
    return render(request, 'post_delete.html', context)
