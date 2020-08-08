from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Category
from marketing.models import Signup


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    context = {
        'queryset':queryset,
    }
    return render(request, 'search_result.html', context)

def index(request):
    featured_posts = Post.objects.filter(featured = True)
    latest_posts = Post.objects.order_by("-timestamp")[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        return redirect('/')


    context = {'featured_posts': featured_posts,
              'latest_posts':latest_posts }
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
        paginated_queryset =  paginator.page(paginator.num_pages)

    latest_posts = Post.objects.order_by("-timestamp")[0:3]
    category_list = Category.objects.all()
    context = {'queryset': paginated_queryset,
               'page_request_var':page_request_var,
               'latest_posts': latest_posts,
               'category_list':category_list,
               }

    return render(request, 'blog.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'item': post}
    return render(request, 'post.html', context)
