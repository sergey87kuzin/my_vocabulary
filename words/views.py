import re
import random

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreationForm
from .models import Word, Rating


pattern_eng = r'([a-z\(\) ]+)'
pattern_rus = r'([а-яё, ]+)'
pattern_page = r'(\d+)'


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('index')
    template_name = 'users/signup.html'


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
    return render(
        request, 'new_words.html',
        {'page': page, 'changes': 'new', 'pages': pages}
    )


@login_required
def get_familiar_list(request):
    word_ids = list(Rating.objects.filter(
        user=request.user, rating__in=[1, 2, 3]
    ).values_list('word', flat=True))
    random.shuffle(word_ids)
    for word_id in word_ids[:15]:
        word = get_object_or_404(Word, id=word_id)
        rating = get_object_or_404(
            Rating, user=request.user, word=word
        )
        rating.rating += 1
        rating.save()
    request.user.familiar_list = word_ids[:15]
    request.user.save()
    return redirect('familiar')


@login_required
def get_new_list(request):
    word_ids = list(Rating.objects.filter(
        user=request.user, rating=0
    ).values_list('word', flat=True))
    random.shuffle(word_ids)
    request.user.new_list = word_ids[:15]
    for word_id in word_ids[:15]:
        word = get_object_or_404(Word, id=word_id)
        rating = get_object_or_404(
            Rating, user=request.user, word=word
        )
        rating.rating += 1
        rating.save()
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
    word_ids = list(Rating.objects.filter(
        user=request.user, rating__gte=3
    ).values_list('word', flat=True))
    random.shuffle(word_ids)
    for word_id in word_ids[:15]:
        word = get_object_or_404(Word, id=word_id)
        rating = get_object_or_404(
            Rating, user=request.user, word=word
        )
        rating.rating += 1
        rating.save()
    request.user.known_list = word_ids[:15]
    request.user.known_idx = 0
    request.user.save()
    redir = request.GET.get('later')
    return redirect(redirs[redir])
