from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import CommentForm
from .forms import MessageForm


def frontpage(request):
    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("contactsuccess")

    else:
        form = MessageForm()

    return render(request, "blog/index.html", {"form": form})


def contactsuccess(request):
    return render(request, "blog/submitted.html")


def workpage(request):
    p = Paginator(Post.objects.all(), 2)
    page = request.GET.get("page")
    post = p.get_page(page)
    postnr = []
    for i in range(post.paginator.num_pages):
        postnr.append(i)
    postnr = map(lambda x: x + 1, postnr)

    return render(request, "blog/work.html", {"post": post, "postnr": postnr})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()

    return render(request, "blog/post.html", {"post": post, "form": form})
