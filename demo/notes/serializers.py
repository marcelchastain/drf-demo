from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Note
