import pytest
from django.db.models import fields

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


def search_field(fields, attname):
    for field in fields:
        if attname == field.attname:
            return field
    return None


class TestWord:

    @pytest.mark.django_db(transaction=True)
    def test_word_model(self, word):
        model_fields = Word._meta.fields
        english_field = search_field(model_fields, 'english')
        assert english_field is not None, (
            'Добавьте английское значение `english` модели `Word`'
        )
        assert type(english_field) == fields.CharField, (
            'Поле `english` модели `Word` должно быть текстовым `CharField`'
        )

        russian_field = search_field(model_fields, 'russian')
        assert russian_field is not None, (
            'Добавьте русское значение `russian` модели `Word`'
        )
        assert type(russian_field) == fields.CharField, (
            'Поле `russian` модели `Word` должно быть текстовым `CharField`'
        )

        new_field = search_field(model_fields, 'is_new')
        assert new_field is not None, (
            'Добавьте русское значение `is_new` модели `Word`'
        )
        assert type(new_field) == fields.BooleanField, (
            'Поле `is_new` модели `Word` должно быть булевым `BooleanField`'
        )

        well_field = search_field(model_fields, 'is_well_known')
        assert well_field is not None, (
            'Добавьте русское значение `is_well_known` модели `Word`'
        )
        assert type(well_field) == fields.BooleanField, (
            'Поле `is_well_known` модели `Word` должно '
            'быть булевым `BooleanField`'
        )

        known_field = search_field(model_fields, 'is_known')
        assert known_field is not None, (
            'Добавьте русское значение `is_known` модели `Word`'
        )
        assert type(known_field) == fields.BooleanField, (
            'Поле `is_known` модели `Word` должно быть булевым `BooleanField`'
        )

        category_field = Word._meta.get_field('category')
        assert category_field is not None, (
            'Добавьте категорию `category` модели `Word`'
        )
        assert type(category_field) == fields.related.ForeignKey, (
            'Свойство `category` модели `Word` должно быть ссылкой на '
            'другую модель `ForeignKey`'
        )
        assert category_field.related_model == Category, (
            'Свойство `category` модели `Word` должно '
            'быть ссылкой на модель `Category`'
        )
        assert category_field.blank, (
            'Свойство `category` модели `Word` должно '
            'быть с атрибутом `blank=True`'
        )
        assert category_field.null, (
            'Свойство `category` модели `Word` должно '
            'быть с атрибутом `null=True`'
        )
        assert category_field.remote_field.related_name == 'words', (
            'Свойство `category` модели `Word` должно '
            'быть с атрибутом `related_name=words`'
        )


class TestCategory:

    # @pytest.mark.django_db(transaction=True)
    def test_category_model(self):
        model_fields = Category._meta.fields
        name_field = search_field(model_fields, 'name')
        assert name_field is not None, (
            'Добавьте название `name` модели `Category`'
        )
        assert type(name_field) == fields.CharField, (
            'Поле `name` модели `Category` должно быть текстовым `CharField`'
        )


class TestUser:

    # @pytest.mark.django_db(transaction=True)
    def test_user_model(self):
        model_fields = User._meta.fields
        staff_field = search_field(model_fields, 'is_staff')
        assert staff_field is not None, (
            'Добавьте роль `is_staff` модели `User`'
        )
        assert type(staff_field) == fields.BooleanField, (
            'Поле `is_staff` модели `User` должно быть булевым `BooleanField`'
        )

        email_field = search_field(model_fields, 'email')
        assert email_field is not None, (
            'Добавьте почту `email` модели `User`'
        )
        assert type(email_field) == fields.EmailField, (
            'Поле `email` модели `User` должно быть `EmailField`'
        )

        username_field = search_field(model_fields, 'username')
        assert username_field is not None, (
            'Добавьте имя пользователя `username` модели `User`'
        )
        assert type(username_field) == fields.CharField, (
            'Поле `username` модели `User` должно быть `CharField`'
        )

        password_field = search_field(model_fields, 'password')
        assert password_field is not None, (
            'Добавьте пароль пользователя `password` модели `User`'
        )
        assert type(password_field) == fields.CharField, (
            'Поле `password` модели `User` должно быть `CharField`'
        )

        new_field = search_field(model_fields, 'new_list')
        assert new_field is not None, (
            'Добавьте новые слова `new_list` модели `User`'
        )
        assert type(new_field) == fields.CharField, (
            'Поле `new_list` модели `User` должно быть `CharField`'
        )

        familiar_field = search_field(model_fields, 'familiar_list')
        assert familiar_field is not None, (
            'Добавьте знакомые слова `familiar_list` модели `User`'
        )
        assert type(familiar_field) == fields.CharField, (
            'Поле `familiar_list` модели `User` должно быть `CharField`'
        )

        known_field = search_field(model_fields, 'known_list')
        assert known_field is not None, (
            'Добавьте известные слова `known_list` модели `User`'
        )
        assert type(known_field) == fields.CharField, (
            'Поле `known_list` модели `User` должно быть `CharField`'
        )

        index_field = search_field(model_fields, 'known_idx')
        assert index_field is not None, (
            'Добавьте индекс перевода `known_idx` модели `User`'
        )
        assert type(index_field) == fields.IntegerField, (
            'Поле `known_idx` модели `User` должно быть `IntegerField`'
        )
