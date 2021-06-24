from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField('signup date', auto_now_add=True)

    def __str__(self):
        return self.name


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField('start date', auto_now_add=True)
