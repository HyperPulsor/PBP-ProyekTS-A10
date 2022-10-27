from django import forms

class FormFaq(forms.Form):
   question = forms.CharField(label='Question', widget=forms.Textarea(attrs={'placeholder': 'New Question'}))
   answer = forms.CharField(label='Answer', widget=forms.Textarea(attrs={'placeholder': 'Answer'}))
