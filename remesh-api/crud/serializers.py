from rest_framework import serializers

from .models import User, Conversation, Message, Thought


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'create_date')


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'title', 'create_date')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'conversation', 'text', 'create_date')


class ThoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = ('id', 'message', 'text', 'create_date')
