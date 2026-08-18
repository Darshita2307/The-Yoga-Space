from django.shortcuts import render,redirect
from . import models
from .forms import BlogForm

# Create your views here.
def blog_create(request):
    blogs=models.Blog.objects.all().order_by('-created_on')
    return render(request,'blog_create.html',{"blogs":blogs} )


def create_blog(request):
    if request.method =='POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            newpost=form.save(commit=False)
            newpost.author=request.user
            newpost.save()
            return redirect('blogs:list')
    else:
        form=BlogForm()
    return render(request,'blog_new.html',{'form':form})              
