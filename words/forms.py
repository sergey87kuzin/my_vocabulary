from django import forms

from .models import Rating


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
