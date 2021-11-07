import pytest
from mixer.backend.django import mixer
from words.models import Word, Rating, Category


@pytest.fixture
def category():
    return Category.objects.create(name='something')


@pytest.fixture
def word(category):
    # from words.models import Word
    return Word.objects.create(
        english='word', russian='слово', category=category
    )


@pytest.fixture
def word_with_rating(user, word):
    # from words.models import Rating
    return Rating.objects.create(word=word, user=user, rating=3)


@pytest.fixture
def few_words_with_rating(user):
    words = [Word(
        id=i, english='english', russian='russian'
    ) for i in range(2400, 2416)]
    Word.objects.bulk_create(words)
    words = Word.objects.all()
    new_ratings = [Rating(
        user=user, word=word, rating=3
    ) for word in words]
    Rating.objects.bulk_create(new_ratings)
    return words[0]
