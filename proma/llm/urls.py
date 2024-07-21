from django.urls import path
from .views import dgu_question, room_test

urlpatterns = [
    path('chatbot/', dgu_question, name='dgu_question'),
    path('room/', room_test, name='room_test'),
]