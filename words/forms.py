from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Rating, User


class RatingCreationForm(forms.ModelForm):
    rating = forms.IntegerField(max_value=5)

    class Meta:
        model = Rating
        fields = ('user', 'word', 'rating')


class RatingChangeForm(forms.ModelForm):
    rating = forms.IntegerField(max_value=5)

    class Meta:
        model = Rating
        fields = ('user', 'word', 'rating')


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class TranslateForm(forms.Form):
    russian = forms.CharField(label='Перевод на русский   ', max_length=100)


class TranslateEnglishForm(forms.Form):
    english = forms.CharField(label='Перевод на английский   ', max_length=100)
