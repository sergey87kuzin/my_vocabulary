from django.urls import path
from . import views
from . import exercises

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/signup/', views.SignUp.as_view(), name='signup'),
    path('create_words/', views.read_words, name='read'),
    path('new_words/', views.show_new_words, name='new'),
    path('get_words/', views.get_new_words, name='get_words'),
    path('get_familiar/', views.get_familiar_list, name='get_familiar'),
    path('get_new/', views.get_new_list, name='get_new'),
    path('get_known/', views.get_known_list, name='get_known'),
    path('familiar_words/', views.show_familiar_words, name='familiar'),
    path('translate/', exercises.translate, name='translate'),
    path(
        'translate_to_english/', exercises.translate_to_english,
        name='translate_to_english'
    ),
    path(
        'word_from_letters', exercises.words_from_letters_english,
        name='word_from_letters_english'
    ),
    path(
        'word_from_letters_rus', exercises.words_from_letters_russian,
        name='word_from_letters_russian'
    )
]
