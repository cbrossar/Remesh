from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/users', views.user_list),
    url(r'^api/conversations', views.conversation_list),
    path('', views.index, name='index'),
]