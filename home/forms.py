from django import forms
from .models import *
  
class TrainingForm(forms.ModelForm):
    class Meta:
        model = img
        fields = ['name', 'Training_Img']

class TrainingForm2(forms.ModelForm):
    class Meta:
        model = img2
        fields = ['name', 'Training_Img']

class TrainingForm3(forms.ModelForm):
    class Meta:
        model = img3
        fields = ['Testing_Img']
