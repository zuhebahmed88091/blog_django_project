from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author':'Zuheb Ahmed',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'May 18, 2022'
    },
    {
        'author':'Linas',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'June 6, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
