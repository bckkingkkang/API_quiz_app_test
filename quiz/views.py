# 데이터베이스로부터 가지고 온 데이터를 가공하여 API 형태로 제공하는 역할
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

@api_view(['GET'])
def helloAPI(request) :
    return Response("Hello World!")

@api_view(['GET'])
def randomQuiz(resquest, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)
