from django.shortcuts import render
from .serializers import ChatbotSerializer, ChatSerializer, RoomTestSerializer, RoomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import chatbot, get_history
from .models import chatting_tb, room_tb
from drf_yasg.utils import swagger_auto_schema


@api_view(['POST'])
def dgu_question(request):
    serializer = ChatbotSerializer(data=request.data)
    if serializer.is_valid():
        room = serializer.data['roomId']
        history = get_history(room)
            # 대화 기록 리스트 반환
        chatting_type = room_tb.objects.get(id=room).room_type

        answer = chatbot(serializer.data['question'], chatting_type, history)
                # 랭체인으로부터 대답을 얻음(모델 : gpt-4o)
        data = {"question": serializer.data['question'], 'answer': answer, 'room': room}
        chat_serializer = ChatSerializer(data=data)
        chat_serializer.is_valid(raise_exception=True)
        chat_serializer.save()
            # 채팅 테이블에 저장
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
        chat_data = chatting_tb.objects.filter(room=room_id).values()
        history = ""
        for i in chat_data:
            # history.append({"human": i['question'], "system": i['answer']})
            history += '[human]:' + i['question'] + ' / [system]:' + i['answer'] + ' / '
        return Response({
            "responseDto": {
                "data": serializer.data,
                "answer": history,
            },
            "error": None,
            "success": True
        }, status=status.HTTP_200_OK)
