from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
# from . import exercises

router_v1 = SimpleRouter()
router_v1.register(r'all_words', views.AllViewSet, basename='all')
router_v1.register('new_words', views.NewViewSet, basename='new')
router_v1.register(
    r'familiar_words', views.FamiliarViewSet, basename='familiar'
)
router_v1.register(
    r'known_words', views.KnownViewSet, basename='known'
)
api_v1_patterns = [
    path('', include(router_v1.urls)),
    path('check_answer/', views.check_words, name='check_words'),
    path('get_word/', views.get_word_for_excercise, name='get_word')
]

urlpatterns = [
    path('v1/', include(api_v1_patterns)),
    # path('', views.index, name='index'),
    # path('auth/signup/', views.SignUp.as_view(), name='signup'),
    # path('create_words/', views.read_words, name='read'),
    # path('new_words/', views.show_new_words, name='new'),
    # path('get_words/', views.get_new_words, name='get_words'),
    # path('get_familiar/', views.get_familiar_list, name='get_familiar'),
    # path('get_new/', views.get_new_list, name='get_new'),
    # path('get_known/', views.get_known_list, name='get_known'),
    # path('familiar_words/', views.show_familiar_words, name='familiar'),
    # path('translate/', exercises.translate, name='translate'),
    # path(
    #     'translate_to_english/', exercises.translate_to_english,
    #     name='translate_to_english'
    # ),
    # path(
    #     'word_from_letters', exercises.words_from_letters_english,
    #     name='word_from_letters_english'
    # ),
    # path(
    #     'word_from_letters_rus', exercises.words_from_letters_russian,
    #     name='word_from_letters_russian'
    # ),
    # path(
    #     'wrong_answer/<int:word_id>/<str:later>/',
    #     views.wrong_answer, name='wrong_answer'
    # )
]
