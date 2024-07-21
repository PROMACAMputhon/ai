from rest_framework import serializers
from .models import chatting_tb

class ChatbotSerializer(serializers.Serializer):
    roomId = serializers.IntegerField()
    chattingType = serializers.IntegerField()
    question = serializers.CharField(max_length=200)

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = chatting_tb
        fields = '__all__'

class RoomTestSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()