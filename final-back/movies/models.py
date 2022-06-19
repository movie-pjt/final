from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=50)
    overview = models.TextField()
    release_date = models.DateField()
    popularity = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    play_time = models.IntegerField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    video_path = models.TextField()
    netflix_path = models.TextField(null=True)
    watcha_path = models.TextField(null=True)
    genres = models.ManyToManyField('Genre', related_name='movies')
    actors = models.ManyToManyField('Actor', related_name='movies')
    directors = models.ManyToManyField('Director', related_name='movies')
    producers = models.ManyToManyField('Producer', related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    def __str__(self):
        return self.title
    


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)


class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


class Director(models.Model):
    director_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Producer(models.Model):
    producer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    title = models.TextField(max_length=40)
    content = models.TextField()
    vote_average = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    
    def __str__(self):
        return self.title

class MovieCount(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_counts")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movie_counts")
    count = models.IntegerField()
