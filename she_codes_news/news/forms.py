from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
            model = NewsStory        
            fields = ['title', 'pub_date', 'content', 'image']
            widgets = {
                'pub_date': forms.DateTimeInput(
                    format=['%d/%m/%Y %H:%M'],
                    attrs={
                        'class': 'form-control',
                        'placeholder':'Select date and time to publish story',
                        'type': 'datetime-local'
        }
    )
}