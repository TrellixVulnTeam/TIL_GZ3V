from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Todo

User = get_user_model() #serializer에서는 이렇게 쓰기를 권장한다.

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed')


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)

class UserSerializer(serializers.ModelSerializer):
    todo_set = TodoSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'todo_set',)