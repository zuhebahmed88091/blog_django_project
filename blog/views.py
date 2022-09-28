from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# from django.http import HttpResponse

def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

#dummy data
# posts = [
#     {
#         'author':'Zuheb Ahmed',
#         'title':'Blog post 1',
#         'content':'First post content',
#         'date_posted':'May 18, 2022'
#     },
#     {
#         'author':'Linas',
#         'title':'Blog post 2',
#         'content':'Second post content',
#         'date_posted':'June 6, 2022'
#     }
# ]

