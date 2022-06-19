from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Count
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Discuss, DiscussComment
from .serializers.discuss import DiscussListSerializer, DiscussSerializer
from .serializers.discuss_comment import DiscussCommentSerializer

@api_view(['GET', 'POST'])
def discuss_list(request):

    def discuss_list():
        discusses = Discuss.objects.annotate(
            discuss_comment_count=Count('discuss_comments', distinct=True),
            choice_a_count=Count('choice_a_users', distinct=True),
            choice_b_count=Count('choice_b_users', distinct=True)
        ).order_by('-pk')    
        serializer = DiscussListSerializer(discusses, many=True)
        return Response(serializer.data)
    
    def create_discuss():
        serializer = DiscussSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return discuss_list()
    elif request.method == 'POST':
        return create_discuss()
    

@api_view(['GET', 'PUT', 'DELETE'])
def discuss_detail(request, discuss_pk):
    discuss = get_object_or_404(Discuss, pk=discuss_pk)

    def discuss_detail():
        serializer = DiscussSerializer(discuss)
        return Response(serializer.data)

    def update_discuss():
        if request.user == discuss.user:
            serializer = DiscussSerializer(instance=discuss, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete_discuss():
        if request.user == discuss.user:
            discuss.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return discuss_detail()
    elif request.method == 'PUT':
        if request.user == discuss.user:
            return update_discuss()
    elif request.method == 'DELETE':
        if request.user == discuss.user:
            return delete_discuss()

@api_view(['POST'])
def choice_a(request, discuss_pk):
    discuss = get_object_or_404(Discuss, pk=discuss_pk)
    user = request.user
    if discuss.choice_a_users.filter(pk=user.pk).exists():
        discuss.choice_a_users.remove(user)
    else:
        if discuss.choice_b_users.filter(pk=user.pk).exists():
            discuss.choice_b_users.remove(user)
        discuss.choice_a_users.add(user)
    serializer = DiscussSerializer(discuss)
    return Response(serializer.data)

@api_view(['POST'])
def choice_b(request, discuss_pk):
    discuss = get_object_or_404(Discuss, pk=discuss_pk)
    user = request.user
    if discuss.choice_b_users.filter(pk=user.pk).exists():
        discuss.choice_b_users.remove(user)
    else:
        if discuss.choice_a_users.filter(pk=user.pk).exists():
            discuss.choice_a_users.remove(user)
        discuss.choice_b_users.add(user)
    serializer = DiscussSerializer(discuss)
    return Response(serializer.data)

@api_view(['POST'])
def create_comment(request, discuss_pk):
    user = request.user
    discuss = get_object_or_404(Discuss, pk=discuss_pk)
    
    serializer = DiscussCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(discuss=discuss, user=user)

        discuss_comments = discuss.discuss_comments.all()
        serializer = DiscussCommentSerializer(discuss_comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, discuss_pk, comment_pk):
    discuss = get_object_or_404(Discuss, pk=discuss_pk)
    discuss_comment = get_object_or_404(DiscussComment, pk=comment_pk)

    def update_comment():
        if request.user == discuss_comment.user:
            serializer = DiscussCommentSerializer(instance=discuss_comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                discuss_comments = discuss.discuss_comments.all()
                serializer = DiscussCommentSerializer(discuss_comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == discuss_comment.user:
            discuss_comment.delete()
            comments = discuss.discuss_comments.all()
            serializer = DiscussCommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()
