import pytest
from django.core.paginator import Page
from django.urls import reverse
# from django.db.models.query import QuerySet

from words.models import Word


# def get_field_context(context, field_type):
#     for field in context.keys():
#         if (field not in ('user', 'request')
#                 and type(context[field]) == field_type):
#             return context[field]
#     return


def try_404(url, client):
    try:
        response = client.get(url)
    except Exception as e:
        assert False, (
            f'Страница `{url}` работает неправильно. Ошибка: `{e}`'
        )

    assert response.status_code != 404, (
        f'Страница `{url}` не найдена, проверьте этот адрес '
        'в *urls.py*'
    )
    return response


class TestContext:

    @pytest.mark.django_db(transaction=True)
    def test_context_auth(self, user_client, few_words_with_rating):
        urls = [
            '/',
            '/new_words/',
            '/familiar_words/',
        ]
        for url in urls:
            response = try_404(url, user_client)

            assert 'page' in response.context, (
                'Проверьте, что передали переменную `page` в контекст страницы'
                f' `{url}`'
            )
            assert isinstance(response.context['page'], Page), (
                'Проверьте, что переменная `page` на странице '
                f'`{url}` типа `Page`'
            )

    @pytest.mark.django_db(transaction=True)
    def test_translate_context_auth(self, user_client, few_words_with_rating):
        response = try_404(reverse('translate'), user_client)

        assert 'word' in response.context, (
            'Проверьте, что передали переменную `word` в контекст страницы'
            f' `{reverse("translate")}`'
        )
        assert isinstance(response.context['word'], Word), (
                'Проверьте, что переменная `word` на странице '
                f'`{reverse("translate")}` типа `Word`'
            )
        assert 'form' in response.context, (
            'Проверьте, что передали переменную `form` в контекст страницы'
            f' `{reverse("translate")}`'
        )
