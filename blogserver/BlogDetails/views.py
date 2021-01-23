from django.shortcuts import render
from django.http import JsonResponse
from BlogDetails.forms import BlogForm
from BlogDetails.models import Blog
# Create your views here.

def postData(request):
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            try:
               return form.save()

            except:
                raise Exception("Some Error Occured")

def getData(request):
    if request.method=='GET':
        blog=Blog.objects.all()
        print(blog)
        return render({
            blog.TopicName
        })
