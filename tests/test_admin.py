from django.contrib.admin.sites import site

try:
    from words.models import Category
except ImportError:
    assert False, 'Не найдена модель Category'
try:
    from words.models import Word
except ImportError:
    assert False, 'Не найдена модель Word'

try:
    from words.models import User
except ImportError:
    assert False, 'Не найдена модель User'


class TestWord:
    def test_word_admin(self):
        admin_site = site

        assert Word in admin_site._registry, (
            'Зарегистрируйте модель `Word` в админской панели'
        )

        admin_model = admin_site._registry[Word]

        assert 'english' in admin_model.list_display, (
            'Добавьте `english` для отображения в списке модели'
            ' административного сайта'
        )
        assert 'russian' in admin_model.list_display, (
            'Добавьте `russian` для отображения в списке модели '
            'административного сайта'
        )

        assert 'english' in admin_model.search_fields, (
            'Добавьте `english` для поиска модели административного сайта'
        )

        assert 'english' in admin_model.list_filter, (
            'Добавьте `english` для фильтрации модели административного сайта'
        )

        assert 'russian' in admin_model.list_filter, (
            'Добавьте `russian` для фильтрации модели административного сайта'
        )

        assert hasattr(admin_model, 'empty_value_display'), (
            'Добавьте дефолтное значение `-пусто-` для пустого поля'
        )
        assert admin_model.empty_value_display == '-пусто-', (
            'Добавьте дефолтное значение `-пусто-` для пустого поля'
        )


class TestCategory:
    def test_category_admin(self):
        admin_site = site

        assert Category in admin_site._registry, (
            'Зарегистрируйте модель `Category` в админской панели'
        )

        admin_model = admin_site._registry[Category]

        assert 'name' in admin_model.list_display, (
            'Добавьте `name` для отображения в списке модели'
            ' административного сайта'
        )

        assert 'name' in admin_model.search_fields, (
            'Добавьте `name` для поиска модели административного сайта'
        )

        assert 'name' in admin_model.list_filter, (
            'Добавьте `name` для фильтрации модели административного сайта'
        )


class TestUser:
    def test_user_admin(self):
        fields = ['email', 'username', 'is_staff']
        admin_site = site

        assert User in admin_site._registry, (
            'Зарегистрируйте модель `User` в админской панели'
        )

        admin_model = admin_site._registry[User]

        for field in fields:
            assert field in admin_model.list_display, (
                f'Добавьте `{field}` для отображения в списке модели'
                ' административного сайта'
            )

        assert 'email' in admin_model.search_fields, (
            'Добавьте `email` для поиска модели административного сайта'
        )

        assert 'email' in admin_model.list_filter, (
            'Добавьте `email` для фильтрации модели административного сайта'
        )
