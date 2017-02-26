from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import PostFormulario


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
                .order_by('published_date')
    template = 'blog/post_list.html'
    context = { 'lista_post': posts }

    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostFormulario(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', post_id=post.pk)
    else:
        form = PostFormulario()
        return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostFormulario(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog.views.post_detail', post_id=post.pk)
    else:
        form = PostFormulario(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


