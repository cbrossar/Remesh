from rest_framework.decorators import api_view
from ..models import Conversation, Message
from ..serializers import ConversationSerializer, MessageSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


@api_view(['GET', 'POST'])
def conversation_list(request):
    if request.method == 'GET':
        conversations = Conversation.objects.all()
        conversation_serializer = ConversationSerializer(conversations, many=True)
        return JsonResponse(conversation_serializer.data, safe=False)

    elif request.method == 'POST':
        conversation_data = JSONParser().parse(request)
        print(conversation_data)
        conversation_serializer = ConversationSerializer(data=conversation_data)
        if conversation_serializer.is_valid():
            conversation_serializer.save()
            return JsonResponse(conversation_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(conversation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def conversation_detail(request, pk):
    try:
        conversation = Conversation.objects.get(pk=pk)
    except Conversation.DoesNotExist:
        return JsonResponse({'message': 'The conversation does not exist'}, status=status.HTTP_404_NOT_FOUND)

    conversation_serializer = ConversationSerializer(conversation)
    data = conversation_serializer.data
    messages = Message.objects.filter(conversation=pk)
    message_serializer = MessageSerializer(messages, many=True)
    data['messages'] = message_serializer.data
    return JsonResponse(data)


@api_view(['POST'])
def conversation_search(request):

    search_data = JSONParser().parse(request)
    conversations = Conversation.objects.filter(title__contains=search_data['search_text'])
    conversation_serializer = ConversationSerializer(conversations, many=True)
    return JsonResponse(conversation_serializer.data, safe=False)
