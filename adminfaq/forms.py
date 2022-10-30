from django import forms
from .models import Faq

class FormFaq(forms.ModelForm):
   class Meta:
      model = Faq
      fields = ['question', 'answer']
      labels = {
            'question': '', 
            'answer': ''
        }
      widgets = {
         'question' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Pertanyaan'}),
         'answer' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Jawaban'}),
      }
