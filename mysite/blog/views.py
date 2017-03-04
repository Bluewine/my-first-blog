from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from .models import *
from .forms import PostFormulario


def post_list(request):
    """
    Lista de todos los post almacenados en la BD.

    Es la pagina inicial.
    """

    if request.user.has_perm('view_specific_permission'):
        posts = Post.objects.filter(published_date__lte=timezone.now()) \
            .order_by('published_date')
        template = 'blog/post_list.html'
        context = {'lista_post': posts}

        return render(request, template, context)
    else:
        return HttpResponse("No tienes permiso adecuado.")


def post_detail(request, post_id):
    """
    Vista de detalle de un post.

    Muestra los detalles de un post seleccionado.

    :param request: Objeto por defecto que recibe una funcion vista.
    :param post_id: Numero de post.
    :return: Una pogina HTML.
    """
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    """
    Vista de nuevos post.

    Es la funcion vista usada para crear nuevos post.

    :param request: Objeto por defecto.
    :return: Una pag HTML
    """
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


