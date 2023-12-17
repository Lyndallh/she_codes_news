from django import forms
from django.forms import ModelForm
from .models import NewsStory
from .models import Comment
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class StoryForm(ModelForm):
    class Meta:

            model = NewsStory        
            fields = ['title', 'pub_date', 'content', 'image']
            labels = {'title':'', 
                      'pub_date':'', 
                      'content':'',
                      'image':''}
            widgets = {
                'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Story Title'}), 
                'pub_date': forms.DateTimeInput(
                    format=['%d/%m/%Y %H:%M'],
                    attrs={
                        'class': 'form-control',
                        'placeholder':'Select date and time to publish story',
                        'type': 'datetime-local'}),
                'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Write your story here....'}),
                'image':forms.URLInput(attrs={'class':'form-control','placeholder':'Image URL'}),
}
            
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']