from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Artwork, ArtworkComment
from .forms import ArtworkForm, ArtworkCommentForm


def gallery_list(request):
    q = request.GET.get("q", "").strip()
    artworks = Artwork.objects.all().prefetch_related("likes")

    if q:
        artworks = artworks.filter(title__icontains=q) | artworks.filter(tags__icontains=q)

    return render(request, "gallery/list.html", {"artworks": artworks, "q": q})


def artwork_detail(request, pk: int):
    artwork = get_object_or_404(Artwork.objects.prefetch_related("likes"), pk=pk)

    # Добавление комментария
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(f"/accounts/login/?next=/gallery/{artwork.id}/")

        comment_form = ArtworkCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.artwork = artwork
            comment.user = request.user
            comment.save()
            messages.success(request, "Комментарий добавлен.")
            return redirect("gallery:detail", pk=artwork.id)
    else:
        comment_form = ArtworkCommentForm()

    comments = artwork.comments.select_related("user").all()

    return render(
        request,
        "gallery/detail.html",
        {
            "artwork": artwork,
            "comment_form": comment_form,
            "comments": comments,
        },
    )


@login_required
def toggle_like(request, pk: int):
    artwork = get_object_or_404(Artwork, pk=pk)

    if request.user in artwork.likes.all():
        artwork.likes.remove(request.user)
        messages.info(request, "Лайк убран.")
    else:
        artwork.likes.add(request.user)
        messages.success(request, "Лайк поставлен ❤️")

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/gallery/"))


@login_required
def comment_delete(request, pk: int):
    comment = get_object_or_404(ArtworkComment, pk=pk)
    artwork_id = comment.artwork_id

    # Удалять может автор комментария или staff
    if comment.user_id != request.user.id and not request.user.is_staff:
        messages.error(request, "Нет прав на удаление комментария.")
        return redirect("gallery:detail", pk=artwork_id)

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Комментарий удалён.")

    return redirect("gallery:detail", pk=artwork_id)


@login_required
def artwork_create(request):
    if request.method == "POST":
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Работа добавлена в галерею.")
            return redirect("gallery:list")
    else:
        form = ArtworkForm()
    return render(request, "gallery/create.html", {"form": form})