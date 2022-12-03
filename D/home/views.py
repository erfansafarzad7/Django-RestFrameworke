from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Answer, Question
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User
from rest_framework import status
from permissions import OwnerOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class Home(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    throttle_scope = 'questions'

    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    """
        Create a new question.

    """
    permission_classes = [IsAuthenticated, ]
    serializer_class = QuestionSerializer

    def post(self, request):
        ser_data = QuestionSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [OwnerOrReadOnly, ]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        ser_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [OwnerOrReadOnly, ]

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response({'message': 'Question Deleted'}, status=status.HTTP_200_OK)

