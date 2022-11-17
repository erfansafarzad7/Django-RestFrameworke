from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Answer, Question
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User
from rest_framework import status


class Home(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def put(self, pk):
        pass

    def delete(self, pk):
        pass

