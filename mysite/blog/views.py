from django.shortcuts import render

from .models import *


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
                .order_by('published_date')
    template = 'blog/post_list.html'
    context = { 'lista_post': posts }

    return render(request, template, context)

