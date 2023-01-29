from rest_framework import serializers
from .models import Word


class WordSerializer(serializers.ModelSerializer):
    isKnown = serializers.SerializerMethodField()

    class Meta:
        exclude = ('is_new', 'is_well_known', 'is_known')
        model = Word

    def get_isKnown(self, obj):
        if obj.is_new:
            return 'is_new'
        if obj.is_well_known:
            return 'is_well_known'
        if obj.is_known:
            return 'is_known'


class WordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'is_new', 'is_well_known', 'is_known')
