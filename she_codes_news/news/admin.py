from django.contrib import admin
from .models import NewsStory, Comment

# Register your models here.
admin.site.register(NewsStory)
admin.site.register(Comment)
