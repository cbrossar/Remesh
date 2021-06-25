import json
from rest_framework import status
from django.test import TestCase, Client
from ..models import Conversation, Message, Thought
from ..serializers import ThoughtSerializer
import collections


# initialize the APIClient app
client = Client()


class GetAllConversationsTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        c1 = Conversation.objects.create(title='Convo1')
        c2 = Conversation.objects.create(title='Convo2')
        m1 = Message.objects.create(conversation=c1, text='Msg1')
        m2 = Message.objects.create(conversation=c1, text='Msg2')
        m3 = Message.objects.create(conversation=c2, text='Msg11')
        m4 = Message.objects.create(conversation=c2, text='Msg22')
        Thought.objects.create(message=m1, text='Integration')
        Thought.objects.create(message=m1, text='Tests')
        Thought.objects.create(message=m1, text='Are')
        Thought.objects.create(message=m2, text='Very')
        Thought.objects.create(message=m2, text='Very')
        Thought.objects.create(message=m3, text='Important')
        Thought.objects.create(message=m4, text='!')

    def test_get_all_thoughts(self):
        # get API response
        response = client.get('/api/thoughts')
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(response.content.decode("utf-8"))

        # get data from db
        thoughts = Thought.objects.all()
        serializer = ThoughtSerializer(thoughts, many=True)
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_1_thought(self):
        # get API response
        response = client.get('/api/thoughts/1')
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(response.content.decode("utf-8"))

        # get data from db
        thought = Thought.objects.get(pk=1)
        serializer = ThoughtSerializer(thought)
        self.assertEqual(data['text'], serializer.data['text'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
