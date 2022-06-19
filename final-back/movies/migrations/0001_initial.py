# Generated by Django 3.2.12 on 2022-05-22 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('overview', models.TextField()),
                ('release_date', models.DateField()),
                ('popularity', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('adult', models.BooleanField()),
                ('play_time', models.IntegerField()),
                ('poster_path', models.TextField()),
                ('backdrop_path', models.TextField()),
                ('video_path', models.TextField()),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
            ],
        ),
    ]
