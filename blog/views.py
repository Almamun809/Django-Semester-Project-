from django.shortcuts import render
from .models import Post


posts = [
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content': 'first post content',
        'date_posted':'August 27, 2018'
    },
    {
        'author':'CoreyMS',
        'title':'Blog Post 2',
        'content': 'first post content',
        'date_posted':'August 27, 2018'
    },
    {
        'author':'CoreyMS',
        'title':'Blog Post 3',
        'content': 'first post content',
        'date_posted':'August 27, 2018'
    },

]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html', {'title':'About'})


def explore(request):
    return render(request,'blog/Explore.html', {'title':'Explore'})