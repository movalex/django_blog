from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Alex Bogomolov',
        'title': 'first blog post',
        'content': 'first post posted!',
        'date_posted': 'April, 20, 2019'
    },
    {
        'author': 'John Doe',
        'title': 'second blog post',
        'content': 'second post posted!',
        'date_posted': 'April, 21, 2019'
    }
]


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
