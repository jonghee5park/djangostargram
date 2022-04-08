from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline, name='timeline'),
    path('user/register', views.register, name='register'),
    path('user/login', views.login_view, name='login_view'),    
    path('user/logout', views.logout_view, name='logout_view'),
    path('upload', views.upload, name='upload'),    
]