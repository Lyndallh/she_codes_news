from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', login_required(views.AddStoryView.as_view()), name='newStory'),
    path('<int:pk>/comment', views.AddCommentView.as_view(), name='addComment'),
]
