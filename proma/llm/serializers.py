from rest_framework import serializers

class ChatbotSerializer(serializers.Serializer):
    chatting_type = serializers.IntegerField()
    question = serializers.CharField(max_length=200)