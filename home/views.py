from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
# Create your views here.


def index(request):
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
    if request.method == 'POST':
        form = TrainingForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            # return redirect('success')
            img_object=form.instance
             
            return render(request, 'training2.html', {'form': form, 'img_obj': img_object})  
    else:
        form = TrainingForm()
    return render(request, 'training2.html', {'form' : form})

def testing(request):
    return render(request, 'testing.html',)