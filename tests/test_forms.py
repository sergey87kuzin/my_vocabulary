import pytest
from django import forms
from django.contrib.auth.forms import UsernameField


def get_field_context(context, field_type):
    for field in context.keys():
        if (field not in ('user', 'request') and
                type(context[field]) == field_type):
            return context[field]
    return


class TestUserForm:

    def test_creation_form(self, client):
        try:
            response = client.get('/auth/signup/')
        except Exception as e:
            assert False, (
                f"Страница `/auth/signup/` работает неправильно. Ошибка: `{e}`"
            )
        if response.status_code in (301, 302):
            response = client.get('/auth/signup/')
        assert response.status_code != 404, (
            'Страница `/auth/signup/` не найдена, '
            'проверьте этот адрес в *urls.py*'
        )
        try:
            from words.forms import CreationForm
        except ImportError:
            assert False, 'Не найдена форма CreationForm в words.form'

        user_form_context = get_field_context(response.context, CreationForm)
        assert user_form_context is not None, (
            'Проверьте, что передали форму пользователя в контекст страницы '
            '`/auth/signup/` типа `CreationForm`'
        )
        assert len(user_form_context.fields) == 4, (
            'Проверьте, что форма пользователя в контекстке страницы '
            '`/auth/signup/` состоит из двух полей'
        )
        assert 'email' in user_form_context.fields, (
            'Проверьте, что форма пользователя в контекстке страницы '
            '`/auth/signup/` содержится поле `email`'
        )
        assert type(
            user_form_context.fields['email']
        ) == forms.fields.EmailField, (
            'Проверьте, что форма пользователя в контекстке страницы '
            '`/auth/signup/` содержит поле `email` типа `EmailField`'
        )
        assert 'username' in user_form_context.fields, (
            'Проверьте, что форма пользователя в контекстке страницы '
            '`/auth/signup/` содержит поле `username`'
        )
        assert type(
            user_form_context.fields['username']
        ) == UsernameField, (
            'Проверьте, что форма пользователя в контекстке страницы '
            '`/auth/signup/` содержится поле `username` типа `UsernameField`'
        )
        assert 'password1' in user_form_context.fields, (
            'Проверьте, что форма пользователя в контекстке страницы '
            '`/auth/signup/` содержит поле `password`'
        )
        assert type(
            user_form_context.fields['password1']
        ) == forms.fields.CharField, (
            'Проверьте, что форма пользователя в контекстке страницы '
            '`/auth/signup/` содержится поле `password` типа `CharField`'
        )


class TestTranslateForm:

    @pytest.mark.django_db(transaction=True)
    def test_translate_form(self, user_client, few_words_with_rating):
        try:
            response = user_client.get('/get_known/')
        except Exception as e:
            assert False, (
                f"Страница `/translate/` работает неправильно. Ошибка: `{e}`"
            )
        if response.status_code in (301, 302):
            response = user_client.get('/translate/')
        assert response.status_code != 404, (
            'Страница `/translate/` не найдена, '
            'проверьте этот адрес в *urls.py*'
        )
        try:
            from words.forms import TranslateForm
        except ImportError:
            assert False, 'Не найдена форма TranslateForm в words.form'

        translate_form_context = get_field_context(
            response.context, TranslateForm
        )
        assert translate_form_context is not None, (
            'Проверьте, что передали форму перевода в контекст страницы '
            '`/translate/` типа `TranslateForm`'
        )
        assert len(translate_form_context.fields) == 1, (
            'Проверьте, что форма комментария в контекстке страницы '
            '`/translation/` состоит из одного поля'
        )
        assert 'russian' in translate_form_context.fields, (
            'Проверьте, что форма комментария в контекстке страницы '
            '`/translate/` содержится поле `russian`'
        )
        assert type(
            translate_form_context.fields['russian']
        ) == forms.fields.CharField, (
            'Проверьте, что форма комментария в контекстке страницы '
            '`/translate/` содержится поле `text` типа `CharField`'
        )
