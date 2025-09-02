from django.urls import path
from . import views

app_name = 'help_requests'

urlpatterns = [
    # Help request endpoints will be added here
    path('help-requests/', views.help_requests_list, name='help_requests_list'),
]
