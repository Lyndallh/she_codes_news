from django.urls import path
from .views import CreateAccountView, AccountView

app_name ='users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>', AccountView.as_view(), name='profile'),
]