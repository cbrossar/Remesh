from rest_framework.decorators import api_view
from ..models import Thought
from ..serializers import ThoughtSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


@api_view(['GET', 'POST'])
def thought_list(request):
    if request.method == 'GET':
        thoughts = Thought.objects.all()
        thought_serializer = ThoughtSerializer(thoughts, many=True)
        return JsonResponse(thought_serializer.data, safe=False)

    elif request.method == 'POST':
        thought_data = JSONParser().parse(request)
        thought_serializer = ThoughtSerializer(data=thought_data)

        if thought_serializer.is_valid():
            thought_serializer.save()
            return JsonResponse(thought_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(thought_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def thought_detail(request, pk):
    try:
        thought = Thought.objects.get(pk=pk)
    except Thought.DoesNotExist:
        return JsonResponse({'thought': 'The thought does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        thought_serializer = ThoughtSerializer(thought)
        return JsonResponse(thought_serializer.data)
