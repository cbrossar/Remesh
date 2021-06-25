from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField('signup date', auto_now_add=True)

    def __str__(self):
        return self.name


class Conversation(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField('start date', auto_now_add=True)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    create_date = models.DateTimeField('date and time sent', auto_now_add=True)


class Thought(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    create_date = models.DateTimeField('date and time sent', auto_now_add=True)
