from rest_framework import serializers
from .models import Publication_API


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication_API
        fields = '__all__'