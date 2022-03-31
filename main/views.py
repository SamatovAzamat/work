import datetime

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin
# from .models import Ism
import random
from django.contrib import messages
# from .forms import IsmForm
from .models import Post, Category, PostLike
from .forms import PostForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from .models import Carousel



def main_index(request):
    request.page_title = _("Bosh sahifa")

    return render(request, 'main/index.html', {
        "carousel": Carousel.objects.filter(status=Carousel.STATUS_ACTIVE).order_by("-order").all(),
        "last_posts": Post.objects.order_by("-id").all()[:4],
        "top_like": Post.objects.order_by("-like")[:4],
        "top_dislike": Post.objects.order_by("-dislike")[:4],
        "top_read": Post.objects.order_by("-read")[:4]
    })


def main_cat(request, pk):

    category = Category.objects.get(id=pk)
    request.page_title = category.name

    request.breadcrumb = [
        [category.name]
    ]

    post_list = Post.objects.filter(category_id=pk).all()

    paginator = Paginator(post_list.order_by('-id'), per_page=3)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, "main/cat.html", context={
        "object_list": page.object_list,
        "page_obj": page,
        "category": category,
        "now": "{:%H:%M:%S}".format(datetime.datetime.now())
    })


def main_rasm(request):
    request.page_title = _("rasm")
    return render(request, "main/rasm.html", context={
    })


def main_video(request):
    sarlavha = _("video")
    return render(request, "main/video.html", context={
        "page_title": sarlavha
    })


def main_audio(request):
    sarlavha = _("audio")
    return render(request, "main/audio.html", context={
        "page_title":sarlavha
    })


def main_menu(request):
    sarlavha = _("Bosh sahifa")
    return render(request, "main/menu.html", context={
        "page_title": sarlavha
    })


@login_required
def main_add_post(request):

    # if not request.user.is_authenticated:
    #     return redirect('main:index')

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()

            messages.success(request, _("Maqola muvaffaqiyatli qo'shildi"))

            return redirect('main:index')

    request.page_title = _("Maqola qo'shish")
    return render(request, 'main/add-post.html', {
        'form': form
    })


@login_required
def main_delete_post(request, pk):
    Post.objects.filter(id=pk).delete()

    messages.success(request, _("Maqola muvaffaqiyatli o'chirildi"))
    return redirect('main:index')


def main_view_post(request, pk):
    post = Post.objects.get(id=pk)
    post.read += 1
    post.save()

    request.page_title = post.subject

    request.breadcrumb = [
        post.subject
    ]

    return render(request, 'main/view.html', {
        'post': post,
        'posts':Post.objects.order_by("?")[:3]
    })


@login_required
def main_edit_post(request, pk):
    if not request.user.is_authenticated:
        return redirect('main:index')

    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            form.save()

            messages.success(request, _("Maqola muvaffaqiyatli o'zgartirildi"))

            return redirect('main:index')

    request.page_title = _("Maqolani tahrirlash")
    request.button_title = _("O'zgartirish")

    return render(request, 'main/edit-post.html', {
        'form': form,
        'post': post
    })


@login_required
def main_like(request, type, id):
    post = Post.objects.get(id=id)

    if PostLike.objects.filter(user=request.user, post=post).exists():
        return redirect(request.GET.get('return', 'main:index'))

    PostLike(user=request.user, post=post).save()

    if type == 'like':
        post.like += 1
    elif type == 'dislike':
        post.dislike += 1

    post.save()

    return redirect(request.GET.get('return', 'main:index'))