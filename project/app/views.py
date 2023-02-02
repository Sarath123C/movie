from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import movie


# Create your views here.
def function(request):
    mov=movie.objects.all()
    return render(request,'index.html',{'film':mov})
def detail(request,id):
    mov=movie.objects.get(id=id)
    return render(request,'detail.html',{'fil':mov})
def add_movie(request):
    if request.method == "POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES.get('img')
        vc=movie(name=name,desc=desc,year=year,img=img)
        vc.save()
    return render(request,'add.html')
def update(request,id):
    movi=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movi)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movi':movi})
def delete(request,id):
    if request.method == "POST":
        dele=movie.objects.get(id=id)
        dele.delete()
        return redirect('/')
    return render(request,'delete.html')