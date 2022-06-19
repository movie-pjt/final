from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Review
from articles.models import Article
from discuss.models import Discuss, DiscussComment
from .models import User

class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'backdrop_path')

    class ReviewSerializer(serializers.ModelSerializer):
        
        # class MovieSerializer(serializers.ModelSerializer):

        #     class Meta:
        #         model = Movie
        #         fields = ('pk', 'title')

        # movie = MovieSerializer()
        
        class UserSerializer(serializers.ModelSerializer):
            
            class Meta:
                model = User
                fields = ('pk', 'username')

        user = UserSerializer(read_only=True)

        class Meta:
            model = Review
            fields = ('id', 'title', 'movie', 'content', 'user', 'vote_average')

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    class DiscussSerializer(serializers.ModelSerializer):

        class Meta:
            model = Discuss
            fields = ('pk', 'title', 'content')

    reviews = ReviewSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)
    discusses = DiscussSerializer(many=True)
    

    class Meta:
        model = get_user_model()
        fields = (
            'pk',
            'username',
            'email',
            'reviews',
            'like_movies',
            'like_articles',
            'articles',
            'discusses',
            )

