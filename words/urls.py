from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/signup/', views.SignUp.as_view(), name='signup'),
    path('create_words/', views.read_words, name='read'),
    path('new_words/', views.show_new_words, name='new'),
    path('get_words/', views.get_new_words, name='get_words'),
    path('familiar_words/', views.show_familiar_words, name='familiar'),
    path('translate/', views.translate, name='translate'),
    path('get_familiar/', views.get_familiar_list, name='get_familiar'),
    path('get_new/', views.get_new_list, name='get_new'),
    path('get_known/', views.get_known_list, name='get_known'),
]
