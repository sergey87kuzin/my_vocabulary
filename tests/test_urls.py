import pytest

from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse


class TestTemplate:
    @pytest.mark.django_db(transaction=True)
    def test_urls_uses_correct_template(
        self, user_client, few_words_with_rating
    ):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            reverse('index'): 'index.html',
            reverse('new'): 'new_words.html',
            reverse('familiar'): 'new_words.html',
            reverse('translate'): 'translate.html',
        }

        for reverse_name, template in templates_url_names.items():
            response = user_client.get(reverse_name)

            assertTemplateUsed(response, template)
