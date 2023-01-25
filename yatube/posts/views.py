from django.shortcuts import get_object_or_404, render

from .models import Group, Post

ten: int = 10


def index(request):
    posts = Post.objects.all()[:ten]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:ten]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
