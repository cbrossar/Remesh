from django.test import TestCase
from .models import User, Conversation, Message, Thought


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="cole")

    def test_create_user(self):
        cole = User.objects.get(name="cole")
        self.assertEqual(cole.name, 'cole')


class ConversationTestCase(TestCase):
    def setUp(self):
        Conversation.objects.create(title="convo")

    def test_create_conversation(self):
        c = Conversation.objects.get(title="convo")
        self.assertEqual(c.title, 'convo')


class MessageTestCase(TestCase):
    def setUp(self):
        c = Conversation.objects.create(title="convo")
        Message.objects.create(conversation_id=c.id, text="msg")

    def test_create_message(self):
        m = Message.objects.get(text="msg")
        self.assertEqual(m.text, 'msg')


class ThoughtTestCase(TestCase):
    def setUp(self):
        c = Conversation.objects.create(title="convo")
        m = Message.objects.create(conversation_id=c.id, text="msg")
        Thought.objects.create(message_id=m.id, text="thinkinggg")

    def test_create_conversation(self):
        t = Thought.objects.get(text="thinkinggg")
        self.assertEqual(t.text, 'thinkinggg')
