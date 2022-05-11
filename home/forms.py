from django import forms
from .models import *
  
class TrainingForm(forms.ModelForm):
  
    class Meta:
        model = img
        fields = ['name', 'Training_Img']