from django.http import HttpResponse
from django.shortcuts import render, redirect
from matplotlib.style import context
from .forms import *
from home.imgcut import imgcut
from home.imgcut2 import imgcut2
from home.imgcut3 import imgcut3
import os
from .models import img,img2,img3
from home.model import mlmodel

# Create your views here.


def index(request):
    img.objects.all().delete()
    img2.objects.all().delete()
    img3.objects.all().delete()
    folder_path=(r'/mnt/d/codes/Handwriting-Classifier/training/imgsep')
    test=os.listdir(folder_path)
    for images in test:
        os.remove(os.path.join(folder_path,images))
    folder_path=(r'/mnt/d/codes/Handwriting-Classifier/training/imgsep2')
    test=os.listdir(folder_path)
    for images in test:
        os.remove(os.path.join(folder_path,images))
    folder_path=(r'/mnt/d/codes/Handwriting-Classifier/imgseptest')
    test=os.listdir(folder_path)
    for images in test:
        os.remove(os.path.join(folder_path,images))
    folder_path=(r'/mnt/d/codes/Handwriting-Classifier/media')
    test=os.listdir(folder_path)
    for images in test:
        os.remove(os.path.join(folder_path,images))
    return render(request, 'index.html',)

def options(request):
    return render(request, 'options.html',)
  
# Create your views here.
def training(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            # return redirect('success')
            img_object=form.instance
            return render(request, 'training.html', {'form': form, 'img_obj': img_object})  
    else:
        form = TrainingForm()
    return render(request, 'training.html', {'form' : form})
  

def training2(request):
    imgcut()
    if request.method == 'POST':
        form = TrainingForm2(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            # return redirect('success')
            img_object=form.instance
            return render(request, 'training2.html', {'form': form, 'img_obj': img_object})  
    else:
        form = TrainingForm2()
    return render(request, 'training2.html', {'form' : form})

def testing(request):
    imgcut2()
    if request.method == 'POST':
        form = TrainingForm3(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            # return redirect('success')
            img_object=form.instance
            imgcut3()
            return render(request, 'testing.html', {'form': form, 'img_obj': img_object})  
    else:
        form = TrainingForm3()
    return render(request, 'testing.html', {'form' : form})

def result(request):
    finalresult=mlmodel()
    if(finalresult== "User1"):
        field_name = 'name'
        obj = img.objects.first()
        name1 = getattr(obj, field_name)
        finalresult=name1
    elif(finalresult=="User2"):
        field_name = 'name'
        obj = img2.objects.first()
        name2 = getattr(obj, field_name)
        finalresult=name2

    return render(request,'result.html',{'result': finalresult})
