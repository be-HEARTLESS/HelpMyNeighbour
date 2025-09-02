from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # User authentication endpoints will be added here
    path('users/me/', views.user_profile, name='user_profile'),
]
