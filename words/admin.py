from django.contrib import admin
from django.contrib.auth.models import Group

from .forms import RatingChangeForm, RatingCreationForm
from .models import (
    User, Category, Word, Rating
)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff',)
    list_filter = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_staff')}),
        ('Lists', {'fields': ('new_list', 'familiar_list', 'known_list')}),
        ('Personal info', {'fields': ('username', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class WordAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'english', 'russian'
    )
    search_fields = ('english',)
    list_filter = ('is_new', 'is_well_known', 'is_known')
    empty_value_display = '-пусто-'


class RatingAdmin(admin.ModelAdmin):
    form = RatingChangeForm
    add_form = RatingCreationForm

    list_display = ('user', 'word', 'rating')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
