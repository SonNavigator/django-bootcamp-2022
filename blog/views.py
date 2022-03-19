from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# from .forms import ContactForm
from .forms import ContactForm

print(ContactForm)

def index(request):
    # Query all posts
    all_posts = Post.objects.all()
    return render(request, 'blog/home.html', {'all_posts': all_posts})


def single_post(request, id):
    # Query one post
    single_post = Post.objects.get(pk=id)
    return render(request, 'blog/single-post.html', {'single_post': single_post})


def contact(request):
    return render(request, 'blog/contact.html')
