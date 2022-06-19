# Generated by Django 3.2.12 on 2022-05-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('director_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('producer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movies.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='movies', to='movies.Director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='producers',
            field=models.ManyToManyField(related_name='movies', to='movies.Producer'),
        ),
    ]