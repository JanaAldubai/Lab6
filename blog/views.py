from django.shortcuts import render
from .models import Blog
# Create your views here.
def blog(request):
    post = Blog.objects.all()
    return render(request, 'blog/Blog.html', {'post':post})