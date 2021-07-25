from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from demo.models import Message
from demo.serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
