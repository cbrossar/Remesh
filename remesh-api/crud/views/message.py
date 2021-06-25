from rest_framework.decorators import api_view
from ..models import Message, Thought
from ..serializers import MessageSerializer, ThoughtSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


@api_view(['GET', 'POST'])
def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        message_serializer = MessageSerializer(messages, many=True)
        return JsonResponse(message_serializer.data, safe=False)

    elif request.method == 'POST':
        message_data = JSONParser().parse(request)
        message_serializer = MessageSerializer(data=message_data)

        if message_serializer.is_valid():
            message_serializer.save()
            return JsonResponse(message_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def message_detail(request, pk):
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return JsonResponse({'message': 'The message does not exist'}, status=status.HTTP_404_NOT_FOUND)

    message_serializer = MessageSerializer(message)
    data = message_serializer.data
    thoughts = Thought.objects.filter(message=pk)
    thought_serializer = ThoughtSerializer(thoughts, many=True)
    data['thoughts'] = thought_serializer.data
    return JsonResponse(data)


@api_view(['POST'])
def message_search(request):

    search_data = JSONParser().parse(request)
    messages = Message.objects.filter(text__contains=search_data['search_text'])
    message_serializer = MessageSerializer(messages, many=True)
    return JsonResponse(message_serializer.data, safe=False)
