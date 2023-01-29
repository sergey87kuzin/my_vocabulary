import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TranslateEnglishForm, TranslateForm
from .models import Word


@login_required
def translate_to_english(request):
    lang = 'russian'
    words_id = request.user.known_list[1:-1].split(', ')
    if len(words_id) == 0:
        return redirect('new')
    idx = request.user.known_idx
    word = get_object_or_404(Word, id=words_id[idx])
    answer = word.english.split(' ')
    form = TranslateEnglishForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data.get('english') in answer:
            if idx == 14:
                request.user.known_idx = 0
                request.user.save()
                return redirect('new')
            request.user.known_idx = idx + 1
            request.user.save()
            return redirect('translate_to_english')
        return redirect(
            'wrong_answer', word_id=word.id, later='english'
        )
    return render(request, 'translate.html', {'form': form,
                                              'lang': lang,
                                              'word': word, })


@login_required
def translate(request):
    lang = 'english'
    words_id = request.user.known_list[1:-1].split(', ')
    if len(words_id) == 0:
        return redirect('new')
    idx = request.user.known_idx
    word = get_object_or_404(Word, id=words_id[idx])
    answers = word.russian.split(' ')
    form = TranslateForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data.get('russian') in answers:
            if idx == 14:
                request.user.known_idx = 0
                request.user.save()
                return redirect('new')
            request.user.known_idx = idx + 1
            request.user.save()
            return redirect('translate')
        return redirect(
            'wrong_answer', word_id=word.id, later='russian'
        )
    return render(request, 'translate.html', {'form': form,
                                              'lang': lang,
                                              'word': word, })


@login_required
def words_from_letters_english(request):
    answers = []
    lang = 'english'
    words_id = request.user.known_list[1:-1].split(', ')
    if len(words_id) == 0:
        return redirect('new')
    idx = request.user.known_idx
    word = get_object_or_404(Word, id=words_id[idx])
    answers = word.russian.split(' ')
    random_word = list(answers[0])
    random.shuffle(random_word)
    rand = '  '.join(random_word)
    form = TranslateForm(request.POST or None)
    template = 'translate_from_letters.html'
    if form.is_valid():
        if form.cleaned_data.get('russian') in answers:
            if idx == 14:
                request.user.known_idx = 0
                request.user.save()
                return redirect('new')
            request.user.known_idx = idx + 1
            request.user.save()
            return redirect('word_from_letters_english')
        return redirect(
            'wrong_answer', word_id=word.id, later='eng_let'
        )
    return render(request, template, {'form': form,
                                      'lang': lang,
                                      'rand': rand,
                                      'word': word, })


@login_required
def words_from_letters_russian(request):
    answers = []
    idx = request.user.known_idx
    lang = 'russian'
    words_id = request.user.known_list[1:-1].split(', ')
    if len(words_id) == 0:
        return redirect('new')
    word = get_object_or_404(Word, id=words_id[idx])
    answers = word.english.split(' ')
    random_word = list(answers[0])
    random.shuffle(random_word)
    rand = '  '.join(random_word)
    form = TranslateEnglishForm(request.POST or None)
    template = 'translate_from_letters.html'
    if form.is_valid():
        if form.cleaned_data.get('english') in answers:
            if idx == 14:
                request.user.known_idx = 0
                request.user.save()
                return redirect('new')
            request.user.known_idx = idx + 1
            request.user.save()
            return redirect('word_from_letters_russian')
        return redirect(
            'wrong_answer', word_id=word.id, later='rus_let'
        )
    return render(request, template, {'form': form,
                                      'lang': lang,
                                      'rand': rand,
                                      'word': word, })
