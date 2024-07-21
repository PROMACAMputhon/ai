from django.shortcuts import render
from .serializers import ChatbotSerializer, ChatSerializer, RoomTestSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import chatbot_kind
from .models import chatting_tb, room_tb
from drf_yasg.utils import swagger_auto_schema


@api_view(['POST'])
def dgu_question(request):
    serializer = ChatbotSerializer(data=request.data)
    if serializer.is_valid():
        answer = chatbot_kind(serializer.data['question'], serializer.data['chattingType'])
        room = serializer.data['roomId']
        data = {"question": serializer.data['question'], 'answer': answer, 'room': room}
        chat_serializer = ChatSerializer(data=data)
        chat_serializer.is_valid(raise_exception=True)
        chat_serializer.save()
        return Response({
            "responseDto" : {
                "data" : serializer.data,
                "answer": answer
            },
            "error":None,
            "success": True
        },status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def room_test(request):
    serializer = RoomTestSerializer(data=request.data)
    if serializer.is_valid():
        room_id = serializer.data['room_id']
        data = chatting_tb.objects.filter(room=room_id).values()
        return Response({
            "responseDto": {
                "data": serializer.data,
                "answer": data
            },
            "error": None,
            "success": True
        }, status=status.HTTP_200_OK)
