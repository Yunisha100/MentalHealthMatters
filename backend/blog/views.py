from django.shortcuts import render
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import AddNewPost
from  django.shortcuts import redirect

# Create your views here.

@login_required(login_url='/account/login/')
def blog(request):
    post = BlogPost.objects.all()
    admin = True
    if request.user.is_staff:
        return render(request,'blog/blog.html',{'post':post,'admin':admin})
    else:    
        return render(request,'blog/blog.html',{'post':post})


@login_required(login_url='/account/login/')
def addnewpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = AddNewPost(request.POST)
            if fm.is_valid():
                bp = BlogPost()
                bp.author = request.user
                bp.title = fm.cleaned_data['title']
                bp.abstract = fm.cleaned_data['abstract']
                bp.post = fm.cleaned_data['post']
                bp.published_date = fm.cleaned_data['published_date']
                bp.save()
                return redirect('/blog/')
        else:
            fm = AddNewPost()
        return render(request,'blog/addnewpost.html',{'form':fm})


@login_required(login_url='/account/login/')
def readmore(request,object_id):
    p = BlogPost.objects.get(id=object_id)
    return render(request,'blog/readmore.html',{'p':p})


@login_required(login_url='/account/login/')
def delete_post(request,object_id):
    if request.method == "POST":
        p = BlogPost.objects.get(id=object_id)
        p.delete()
        return redirect('/blog/')

        
@login_required(login_url='/account/login/')
def update_post(request,object_id):
    if request.method == "POST":
        bp = BlogPost.objects.get(id=object_id)
        fm = AddNewPost(request.POST,instance=bp)
        if fm.is_valid():
            fm.save()
            return redirect('/blog/')
    else:
        bp = BlogPost.objects.get(id=object_id)
        fm = AddNewPost(instance=bp)
    
    return render(request,'blog/updatepost.html',{'form':fm})