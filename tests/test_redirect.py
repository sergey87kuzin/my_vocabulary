import pytest


class TestRedirect:

    def test_not_auth_redirect(self, client):
        urls = [
            '/new_words/',
            '/get_words/',
            '/familiar_words/',
            '/get_familiar/',
            '/translate/',
            '/get_new/',
            '/get_known/'
        ]
        for url in urls:
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

            assert response.status_code in (301, 302), (
                'Проверьте, что вы переадресуете пользователя со страницы '
                '`{url}` на страницу авторизации, если он не авторизован'
            )

            assert response.url.startswith('/auth/login'), (
                'Проверьте, что перенаправляете на страницу регистрации '
                '`/auth/login/`'
            )

    @pytest.mark.django_db(transaction=True)
    def test_auth_not_redirect(self, user_client, few_words_with_rating):
        urls = [
            '/new_words/',
            '/familiar_words/',
            '/translate/',
        ]
        for url in urls:
            try:
                response = user_client.get(url)
            except Exception as e:
                assert False, (
                    f'Страница `{url}` работает неправильно. Ошибка: `{e}`'
                )

            assert response.status_code != 404, (
                f'Страница `{url}` не найдена, проверьте этот адрес '
                'в *urls.py*'
            )

            assert response.status_code not in (301, 302), (
                'Проверьте, что вы не переадресуете пользователя со страницы '
                '`{url}` на страницу авторизации, если он авторизован'
            )

    @pytest.mark.django_db(transaction=True)
    def test_auth_redirect(self, user_client):
        urls = [
            '/get_words/',
            '/get_familiar/',
            '/get_new/',
            '/get_known/'
        ]
        for url in urls:
            try:
                response = user_client.get(url)
            except Exception as e:
                assert False, (
                    f'Страница `{url}` работает неправильно. Ошибка: `{e}`'
                )

            assert response.status_code != 404, (
                f'Страница `{url}` не найдена, проверьте этот адрес '
                'в *urls.py*'
            )

            assert response.status_code in (301, 302), (
                'Проверьте, что вы переадресуете пользователя со страницы '
                '`{url}` на страницу задания, если он авторизован'
            )
