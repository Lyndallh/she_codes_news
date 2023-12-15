from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    # path('add-story/', login_required(views.AddStoryView.as_view()), name='newStory'),
    path('add-story/',(views.AddStoryView.as_view()), name='newStory'),
    path('<int:pk>/comment', views.AddCommentView.as_view(), name='addComment'),
    path('author/<int:pk>', views.AuthorView.as_view(), name='author'),
]
