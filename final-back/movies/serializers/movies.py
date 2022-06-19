from rest_framework import serializers
from ..models import Movie, Actor, Director, Producer, Genre, Review
from django.contrib.auth import get_user_model

User = get_user_model()


class MovieListSerializer(serializers.ModelSerializer):
    
    like_count = serializers.IntegerField()
    
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'popularity',
            'poster_path',
            'vote_average',
            'release_date',
            'like_count',
            )

class MovieSerializer(serializers.ModelSerializer):

    class ActorforMovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('name', )

    class DirectorforMovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Director
            fields = ('name', )
    
    class ProducerforMovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Producer
            fields = ('name', )

    class GenreforMovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('name', )

    class ReviewforMovieSerializer(serializers.ModelSerializer):

        class UserforReviewSerializer(serializers.ModelSerializer):
            
            class Meta:
                model = User
                fields = ('pk', 'username')
                
        user = UserforReviewSerializer(read_only=True)
        class Meta:
            model = Review
            fields = '__all__'

    actors = ActorforMovieSerializer(many=True)
    directors = DirectorforMovieSerializer(many=True)
    producers = ProducerforMovieSerializer(many=True)
    genres = GenreforMovieSerializer(many=True)
    reviews = ReviewforMovieSerializer(many=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)
    isLiked = serializers.BooleanField()


    class Meta:
        model = Movie
        fields = '__all__'
        
        
class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('pk', 'username')
            
    # user = UserSerializer(read_only=True)
    # like_count = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'like_users')

class RecommendMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date', 'poster_path')