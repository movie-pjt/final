from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from movies.serializers.movie_count import MovieCountSerializer
from .serializers.movies import MovieListSerializer, MovieSerializer, RecommendMovieSerializer, ReviewSerializer
from .models import Movie, Genre, Actor, Director, Producer, Review, MovieCount
import requests
from rest_framework import status
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import csv

User = get_user_model()


# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.annotate(
        like_count = Count('like_users', distinct=True)
    )
    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.isLiked = (request.user in movie.like_users.all())
    serializer = MovieSerializer(movie)

    return Response(serializer.data)


@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        movie.isLiked = False
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        movie.isLiked = True
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    def review_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    
    def delete_review():
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    if request.method == 'GET':
        return review_detail()
    
    elif request.method == 'PUT':
        return update_review()
    
    elif request.method == 'DELETE':
        return delete_review()


@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
@api_view(['POST'])
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        review.like_users.add(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


@api_view(['POST'])
def movie_count(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if MovieCount.objects.filter(movie=movie, user=user).exists():
        movie_count = MovieCount.objects.filter(movie=movie, user=user)[0]
        serializer = MovieCountSerializer(movie_count, data=request.data)
    else:
        serializer = MovieCountSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def recommendations(request):
    user = request.user
    movies = Movie.objects.all()
    db_dict = {
        'user_id':[],
        'movie_id':[]
    }
    for movie in movies:
        for like_user in movie.like_users.all():
            db_dict['movie_id'].append(movie.pk)
            db_dict['user_id'].append(like_user.pk)
    df = pd.DataFrame(db_dict)
    movie_user_vec = pd.crosstab(df.movie_id, df.user_id)
    user_movie_vec = pd.crosstab(df.user_id, df.movie_id)
    

    # 영화 기반
    similarity_rate_movie_user = cosine_similarity(movie_user_vec, movie_user_vec)
    # 사용자 기반
    similarity_rate_user_movie = cosine_similarity(user_movie_vec, user_movie_vec)

    similarity_rate_movie_user_df = pd.DataFrame(
    data=similarity_rate_movie_user,
    index=movie_user_vec.index,
    columns=movie_user_vec.index
    )
    similarity_rate_user_movie_df = pd.DataFrame(
        data=similarity_rate_user_movie,
        index=user_movie_vec.index,
        columns=user_movie_vec.index
    )


    threshold = 0.4
    rating=similarity_rate_user_movie_df[user.pk].sort_values(ascending=False).drop(user.pk)

    users = rating[(rating > threshold) & (rating < 1)]
    
    result = []
    for user_id in users.keys():
        similar_user = get_object_or_404(User, pk=user_id)
        movies = similar_user.like_movies.all()

        for movie in movies:
            if movie.like_users.filter(pk=user.pk).exists():
                pass
            else:
                result.append(movie.pk)
    
    serializer = RecommendMovieSerializer(Movie.objects.filter(pk__in=result), many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)