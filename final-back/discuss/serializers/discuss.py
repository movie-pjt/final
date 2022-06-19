from rest_framework import serializers
from django.contrib.auth import get_user_model

from .discuss_comment import DiscussCommentSerializer

from ..models import Discuss

User = get_user_model()

class DiscussSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    discuss_comments = DiscussCommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    choice_a_users = UserSerializer(many=True, read_only=True)
    choice_b_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Discuss
        fields = ('pk', 'user', 'title', 'choice_a', 'choice_b', 'discuss_comments', 'choice_a_users', 'choice_b_users',
                  'img','content')

class DiscussListSerializer(serializers.ModelSerializer):
    
    choice_a_count = serializers.IntegerField()
    choice_b_count = serializers.IntegerField()
    discuss_comment_count = serializers.IntegerField()

    class Meta:
        model = Discuss
        fields = ('pk', 'user', 'title', 'choice_a_count', 'choice_b_count', 'discuss_comment_count',
                  'img','content')