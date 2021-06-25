from django.urls import path
from django.conf.urls import url
from .views import views, user, conversation, message, thought

urlpatterns = [
    url(r'^api/users$', user.user_list),
    url(r'^api/users/(?P<pk>[0-9]+)$', user.user_detail),
    url(r'^api/conversations$', conversation.conversation_list),
    url(r'^api/conversations/(?P<pk>[0-9]+)$', conversation.conversation_detail),
    url(r'^api/conversations/search', conversation.conversation_search),
    url(r'^api/messages$', message.message_list),
    url(r'^api/messages/(?P<pk>[0-9]+)$', message.message_detail),
    url(r'^api/messages/search/*', message.message_search),
    url(r'^api/thoughts$', thought.thought_list),
    url(r'^api/thoughts/(?P<pk>[0-9]+)$', thought.thought_detail),
    path('', views.index, name='index'),
]