from django.urls import path
from .views import dgu_question

urlpatterns = [
    path('chatbot/', dgu_question, name='dgu_question'),
]