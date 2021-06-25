import json
from rest_framework import status
from django.test import TestCase, Client
from ..models import Conversation, Message
from ..serializers import MessageSerializer
import collections


# initialize the APIClient app
client = Client()


class GetAllMessagesTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        c1 = Conversation.objects.create(title='Convo1')
        c2 = Conversation.objects.create(title='Convo2')
        Message.objects.create(conversation=c1, text='Msg1')
        Message.objects.create(conversation=c1, text='Msg2')
        Message.objects.create(conversation=c2, text='Msg11')
        Message.objects.create(conversation=c2, text='Msg22')

    def test_get_all_messages(self):
        # get API response
        response = client.get('/api/messages')
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(response.content.decode("utf-8"))

        # get data from db
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_1_message(self):
        # get API response
        response = client.get('/api/messages/1')
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(response.content.decode("utf-8"))

        # get data from db
        message = Message.objects.get(pk=1)
        serializer = MessageSerializer(message)
        self.assertEqual(data['text'], serializer.data['text'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_messages(self):
        search_text = '1'

        # get API response
        response = client.post('/api/messages/search', dict(conversation=1, search_text=search_text),
                               content_type="application/json")
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(response.content.decode("utf-8"))

        # get data from db
        message = Message.objects.filter(conversation=1).filter(text__contains=search_text)
        serializer = MessageSerializer(message, many=True)
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_messages_dne(self):
        search_text = 'dne'

        # get API response
        response = client.post('/api/messages/search', dict(conversation=1, search_text=search_text),
                               content_type="application/json")
        data = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(response.content.decode("utf-8"))

        # get data from db
        message = Message.objects.filter(conversation=1).filter(text__contains=search_text)
        serializer = MessageSerializer(message, many=True)
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
