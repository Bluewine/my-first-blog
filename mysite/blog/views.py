from django.shortcuts import render, get_object_or_404

from .models import *


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
                .order_by('published_date')
    template = 'blog/post_list.html'
    context = { 'lista_post': posts }

    return render(request, template, context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})