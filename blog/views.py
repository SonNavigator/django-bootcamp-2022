from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    # Table.objects.method()
    # Query all posts
    all_posts = Post.objects.all()
    name = "Top"
    return render(request, 'blog/index.html', {
        'all_posts': all_posts, 
        'name': name
        }
    )


def about(request):
    return render(request, 'blog/about.html')















