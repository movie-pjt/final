from django.db import models
from django.conf import settings

# Create your models here.

class Discuss(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discusses')
    choice_a = models.CharField(max_length=100)
    choice_b = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    content = models.CharField(max_length=200)
    # choice_a_img = models.CharField(max_length=100)
    # choice_b_img = models.CharField(max_length=100)
    choice_a_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="choice_a")
    choice_b_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="choice_b")
    
    def __str__(self):
        return self.title
    

class DiscussComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discuss_comments')
    discuss = models.ForeignKey(Discuss, on_delete=models.CASCADE, related_name='discuss_comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    