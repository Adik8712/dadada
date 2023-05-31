from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def index(request):
    all_data = Post.objects.all()
    return render(request, "home/index.html", {"context": all_data})


def insert_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()

    return render(request, "insert/index.html", {"form": form})
