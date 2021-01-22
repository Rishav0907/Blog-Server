from django.shortcuts import render
from BlogDetails.forms import BlogForm
# Create your views here.

def postData(request):
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            try:
               return form.save()

            except:
                raise Exception("Some Error Occured")

# def getData(request):
