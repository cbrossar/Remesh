from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import User, Conversation
from .serializers import UserSerializer, ConversationSerializer
from django.http.response import JsonResponse


def index(request):
    return HttpResponse("Hello, world!")


@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':

        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)


@api_view(['GET'])
def conversation_list(request):
    if request.method == 'GET':

        conversations = Conversation.objects.all()
        conversation_serializer = ConversationSerializer(conversations, many=True)
        return JsonResponse(conversation_serializer.data, safe=False)
