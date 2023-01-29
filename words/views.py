import random
import re
import json
import math

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .forms import CreationForm
from .models import Rating, Word
from .serializers import WordCreateSerializer, WordSerializer

pattern_eng = r'([a-z\(\) ]+)'
pattern_rus = r'([а-яё, ]+)'
pattern_page = r'(\d+)'


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('index')
    template_name = 'users/signup.html'


class WordsViewSet(viewsets.GenericViewSet, ListModelMixin, UpdateModelMixin):
    pass


class AllViewSet(WordsViewSet):
    queryset = Word.objects.all()
    lookup_field = 'id'
    pagination_class = PageNumberPagination
    # serializer_class = WordSerializer

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return WordCreateSerializer
        return WordSerializer


class NewViewSet(WordsViewSet):
    queryset = Word.objects.filter(is_new=True)
    lookup_field = 'id'
    serializer_class = WordSerializer
    pagination_class = PageNumberPagination


class FamiliarViewSet(WordsViewSet):
    queryset = Word.objects.filter(is_well_known=True)
    lookup_field = 'id'
    serializer_class = WordSerializer
    pagination_class = PageNumberPagination


class KnownViewSet(WordsViewSet):
    queryset = Word.objects.filter(is_known=True)
    lookup_field = 'id'
    serializer_class = WordSerializer
    pagination_class = PageNumberPagination


@api_view(['post'])
def check_words(request):
    # with open('request.json', 'w') as f:
    #     json.dump(
    #         obj=request, fp=f, ensure_ascii=False, indent=2,
    #         separators=(',', ': ')
    #     )
    word_id = request.data.get('id')
    answer = request.data.get('answer')
    word = Word.objects.get(id=word_id)
    if answer in word.russian or answer in word.english:
        return Response('Верно')
    return Response(f'Неверно, {word.english} - {word.russian}')


@api_view(['get'])
def get_word_for_excercise(request):
    words = Word.objects.filter(is_known=True)
    index = math.floor(len(words) * random.random())
    word = words[index]
    serializer = WordSerializer(word)
    return Response(serializer.data)


# ---------------------------------------------------------------------------------- #

def index(request):
    word_list = Word.objects.all()
    has_words = '-'
    if request.user.id is not None:
        if Rating.objects.filter(user=request.user).exists():
            has_words = '+'
    paginator = Paginator(word_list, 10)
    num_pages = paginator.num_pages
    page_no = (request.GET.get('page'))
    if page_no is not None:
        if num_pages <= 15 or page_no <= 8:  # case 1 and 2
            pages = [x for x in range(1, min(num_pages + 1, 15))]
        elif page_no > num_pages - 8:  # case 4
            pages = [x for x in range(num_pages - 14, num_pages + 1)]
        else:  # case 3
            pages = [x for x in range(page_no - 7, page_no + 8)]
    else:
        pages = [x for x in range(1, min(num_pages + 1, 15))]
    page = paginator.get_page(page_no)
    return render(
        request, 'index.html',
        {'page': page, 'pages': pages, 'has_words': has_words}
    )


def read_words(request):
    words = []
    with open('enrus.txt', 'r') as f:
        for i in range(5000):
            try:
                line = f.readline()
                english = re.search(pattern_eng, line).group(0)
                russian = re.search(pattern_rus, line).group(0)
                words.append(Word(english=english, russian=russian))
            except Exception:
                print('все слова извлечены')
        f.close()
    Word.objects.bulk_create(words)
    return redirect('index')


@login_required
def get_new_words(request):
    user = request.user
    words = list(Word.objects.all())
    ratings = [Rating(user=user, word=word, rating=0) for word in words]
    Rating.objects.bulk_create(ratings)
    return redirect('new')


@login_required
def show_new_words(request):
    queryset = []
    word_ids = request.user.new_list[1:-1].split(', ')
    if len(word_ids) == 0:
        return redirect('get_new')
    for word_id in word_ids:
        word = get_object_or_404(Word, id=word_id)
        queryset.append(word)
    paginator = Paginator(queryset, 1)
    num_pages = paginator.num_pages
    page_no = (request.GET.get('page'))
    if page_no is not None:
        if num_pages <= 15 or page_no <= 8:  # case 1 and 2
            pages = [x for x in range(1, min(num_pages + 1, 16))]
        elif page_no > num_pages - 8:  # case 4
            pages = [x for x in range(num_pages - 14, num_pages + 1)]
        else:  # case 3
            pages = [x for x in range(page_no - 7, page_no + 8)]
    else:
        pages = [x for x in range(1, min(num_pages + 1, 16))]
    page = paginator.get_page(page_no)
    buttons_under_word(request)
    return render(
        request, 'new_words.html',
        {'page': page, 'changes': 'new', 'pages': pages}
    )


@login_required
def show_familiar_words(request):
    queryset = []
    word_ids = request.user.familiar_list[1:-1].split(', ')
    if len(word_ids) == 0:
        return redirect('new')
    print(len(word_ids))
    for word_id in word_ids:
        word = get_object_or_404(Word, id=word_id)
        queryset.append(word)
    paginator = Paginator(queryset, 1)
    num_pages = paginator.num_pages
    page_no = (request.GET.get('page'))
    if page_no is not None:
        if num_pages <= 15 or page_no <= 8:  # case 1 and 2
            pages = [x for x in range(1, min(num_pages + 1, 16))]
        elif page_no > num_pages - 8:  # case 4
            pages = [x for x in range(num_pages - 14, num_pages + 1)]
        else:  # case 3
            pages = [x for x in range(page_no - 7, page_no + 8)]
    else:
        pages = [x for x in range(1, min(num_pages + 1, 16))]
    page = paginator.get_page(page_no)
    buttons_under_word(request)
    return render(
        request, 'new_words.html',
        {'page': page, 'changes': 'new', 'pages': pages}
    )


@login_required
def get_familiar_list(request):
    # word_ids = list(Rating.objects.filter(
    #     user=request.user, rating__in=[1, 2, 3]
    # ).values_list('word', flat=True))
    # for word_id in word_ids[:15]:
    #     word = get_object_or_404(Word, id=word_id)
    #     rating = get_object_or_404(
    #         Rating, user=request.user, word=word
    #     )
    #     rating.rating += 1
    #     rating.save()
    words = Word.objects.filter(is_well_known=True).values_list('id')
    word_ids = [x[0] for x in words]
    random.shuffle(word_ids)
    request.user.familiar_list = word_ids[:15]
    request.user.save()
    return redirect('familiar')


@login_required
def get_new_list(request):
    words = Word.objects.filter(is_new=True).values_list('id')
    word_ids = [x[0] for x in words]
    random.shuffle(word_ids)
    request.user.new_list = word_ids[:15]
    request.user.save()
    return redirect('new')


@login_required
def get_known_list(request):
    redirs = {
        'english': 'translate_to_english',
        'russian': 'translate',
        'eng_let': 'word_from_letters_english',
        'rus_let': 'word_from_letters_russian'
    }
    words = Word.objects.filter(is_known=True).values_list('id')
    word_ids = [x[0] for x in words]
    random.shuffle(word_ids)
    request.user.known_list = word_ids[:15]
    request.user.known_idx = 0
    request.user.save()
    redir = request.GET.get('later')
    return redirect(redirs[redir])


@login_required
def wrong_answer(request, word_id, later):
    word = Word.objects.get(id=word_id)
    context = {'later': later, 'word': word}
    return render(request, 'wrong_answer.html', context=context)


def change_status(request, button, is_new, is_med, is_well):
    curr_word = Word.objects.get(id=request.POST[button])
    curr_word.is_new = is_new
    curr_word.is_well_known = is_med
    curr_word.is_known = is_well
    curr_word.save()


def buttons_under_word(request):
    if 'low' in request.POST:
        change_status(request, 'low', True, False, False)
    if 'medium' in request.POST:
        change_status(request, 'medium', False, True, False)
    if 'high' in request.POST:
        change_status(request, 'high', False, False, True)
