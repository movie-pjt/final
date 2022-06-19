from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.serializers.movies import MovieSerializer
from ..models import MovieCount, Movie

User = get_user_model()

class MovieCountSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieCount
        fields = ('pk', 'user', 'movie', 'count')
        read_only_fields = ('movie', 'user')
