from django.contrib import admin
from .models import MovieCount, Movie, Actor, Director, Producer, Review

class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title',
    )
    
# Register your models here.
admin.site.register(MovieCount)
admin.site.register(Actor)
admin.site.register(Producer)
admin.site.register(Review)
admin.site.register(Movie, MovieAdmin)
