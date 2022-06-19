from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import DiscussComment

User = get_user_model()

class DiscussCommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = DiscussComment
        fields = ('pk', 'user', 'content', 'discuss',)
        read_only_fields = ('discuss', )
