from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email=email, is_staff=True, password=password,
            **extra_fields
        )

    def all(self):
        return self.get_queryset()


class User(AbstractBaseUser):
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    words = models.ManyToManyField(
        'Word',
        related_name='users',
        through='Rating',
        blank=True,
        null=True
    )
    username = models.CharField(max_length=150, unique=True,
                                verbose_name='username')
    password = models.CharField(max_length=150, verbose_name='password',
                                blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    USER_ID_FIELD = 'id'
    REQUIRED_FIELDS = ['password', 'username']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Word(models.Model):
    english = models.CharField(max_length=30)
    russian = models.CharField(max_length=30)
    is_new = models.BooleanField(default=True)
    is_well_known = models.BooleanField(default=False)
    is_known = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='words',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('english',)

    def __str__(self):
        return self.english


class Rating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_word_rating',
        verbose_name='пользователь'
    )
    word = models.ForeignKey(
        Word,
        on_delete=models.CASCADE,
        related_name='word_rating',
        verbose_name='слово'
    )
    rating = models.IntegerField(default=0)

    class Meta:
        ordering = ('user', 'word')

    def __str__(self):
        return f'{self.user.username} + {self.word.english} = {self.rating}'
