from django.shortcuts import render, redirect
from .models import Post
from marketing.models import Signup


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
    return render(request, 'blog.html', {})


def post(request):
    return render(request, 'post.html', {})
