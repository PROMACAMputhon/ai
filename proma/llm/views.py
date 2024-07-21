from django.shortcuts import render
from .serializers import ChatbotSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import chatbot_kind


@api_view(['POST'])
def dgu_question(request):
    serializer = ChatbotSerializer(data=request.data)
    if serializer.is_valid():
        answer = chatbot_kind(serializer.data['question'], serializer.data['chatting_type'])
        return Response({
            "responseDto" : {
                "data" : serializer.data,
                "answer": answer
            },
            "error":None,
            "success": True
        },status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)