from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView
# Create your views here.

def home(request):
   return  render (request,"blog/home.html",context={"posts":Post.objects.all()})

class PostListView(ListView):
   model=Post
   template_name="blog/home.html"
   ordering=["-time"]
   context_object_name="posts"

class PostDetailView(DetailView):
   model=Post
   ordering=["-time"]

def about(request):
   return render(request,"blog/about.html")

   

