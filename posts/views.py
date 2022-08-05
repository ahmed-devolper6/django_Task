from django.shortcuts import render
from .models import posts
# Create your views here.
def all_posts(request):
    post = posts.objects.all()
    return render(request ,"blog.html" ,{"ahmed":post})
def single_post(request , id):
    post = posts.objects.get(id = id)
    return render(request,"single.html",{"single_post": post})