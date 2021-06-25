import json
from rest_framework import status
from django.test import TestCase, Client
from ..models import Conversation
from ..serializers import ConversationSerializer
import collections


# initialize the APIClient app
client = Client()


class GetAllConversationsTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        Conversation.objects.create(title='Convo1')
        Conversation.objects.create(title='Convo2')
        Conversation.objects.create(title='Remesh3')
        Conversation.objects.create(title='Remesh4')

    def test_get_all_conversations(self):
        # get API response
        response = client.get('/api/conversations')
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(response.content.decode("utf-8"))

        # get data from db
        conversations = Conversation.objects.all()
        serializer = ConversationSerializer(conversations, many=True)
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_1_conversation(self):
        # get API response
        response = client.get('/api/conversations/1')
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(response.content.decode("utf-8"))

        # get data from db
        conversation = Conversation.objects.get(pk=1)
        serializer = ConversationSerializer(conversation)
        self.assertEqual(data['title'], serializer.data['title'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_conversations(self):
        search_text = 'Remesh'

        # get API response
        response = client.post('/api/conversations/search', dict(search_text=search_text),
                               content_type="application/json")
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(response.content.decode("utf-8"))

        # get data from db
        conversation = Conversation.objects.filter(title__contains=search_text)
        serializer = ConversationSerializer(conversation, many=True)
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_conversations_dne(self):
        search_text = 'dne'

        # get API response
        response = client.post('/api/conversations/search', dict(search_text=search_text),
                               content_type="application/json")
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(response.content.decode("utf-8"))

        # get data from db
        conversation = Conversation.objects.filter(title__contains=search_text)
        serializer = ConversationSerializer(conversation, many=True)
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
