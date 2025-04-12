from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PlayerProgress, Option, Level, Quiz, QuizQuestion, Question
from .serializers import PlayerProgressSerializer, LevelSerializer, QuestionSerializer, QuizSerializer


class StartGameView(APIView):

    def post(self, request, pk=None):
        level = Level.objects.get(id=pk)
        questions = level.quizzes.all()
        quiz = Quiz.objects.filter(id=pk)

        PlayerProgress.objects.create(
            uuid=request.data.get('uuid'),
            level=level,  # Привязываем прогресс к уровню
            points=0,
            finished=False
        )

        question_data = [{
            "question_id": q.id,
            "text": q.question,
        } for q in questions]

        quizzes = [{
            "question_id": q.id,
            "text": q.question,
        } for q in quiz]

        return Response({
            "message": "Level started",
            "questions": question_data,
            "quiz" : quizzes
        })

class GetOptions(APIView):

    def get(self, request, pk=None):
        options = Option.objects.filter(quiz=pk)

        question_data = [{
            "question_id": q.id,
            "text": q.text,
        } for q in options]

        return Response({
            "message": "Level started",
            "questions": question_data
        })

class GetQuizQuestionView(APIView):

    def get(self, request, pk=None):
        options = QuizQuestion.objects.filter(quiz=pk)

        question_data = [{
            "question_id": q.id,
            "text": q.text,
        } for q in options]

        return Response({
            "message": "Level started",
            "questions": question_data
        })

class AnswerOptionViewSet(APIView):
    queryset = PlayerProgress.objects.all()
    serializer_class = PlayerProgressSerializer

    def post(self, request):
        uuid = request.data.get('uuid')
        if not uuid:
            return Response({"error": "UUID не предоставлен"}, status=400)

        try:
            progress = PlayerProgress.objects.get(uuid=uuid)
        except PlayerProgress.DoesNotExist:
            progress = PlayerProgress(uuid=uuid)
        option_id = request.data.get('option_id')

        try:
            option = Option.objects.get(id=option_id)
        except (Question.DoesNotExist, Option.DoesNotExist):
            return Response({'error': 'Question or Option not found'}, status=404)

        progress.points += option.points
        progress.save()

        return Response({
            "added_points": option.points,
            "total_points": progress.points
        }
    )

class QuizQuestionViewSet(APIView):
    queryset = PlayerProgress.objects.all()
    serializer_class = PlayerProgressSerializer

    def post(self, request):
        uuid = request.data.get('uuid')
        if not uuid:
            return Response({"error": "UUID не предоставлен"}, status=400)

        try:
            progress = PlayerProgress.objects.get(uuid=uuid)
        except PlayerProgress.DoesNotExist:
            progress = PlayerProgress(uuid=uuid)
        quiz_question_id = request.data.get('quiz_question_id')

        try:
            option = QuizQuestion.objects.get(id=quiz_question_id)
        except (Question.DoesNotExist, Option.DoesNotExist):
            return Response({'error': 'Question not found'}, status=404)
        if (option.is_correct):
            progress.quizPoints += 1
            progress.save()



        return Response({
            "message": "Выбор применён",
            "quizpoints": progress.quizPoints
        }
    )

class ResultView(APIView):
    def get(self, request, pk=None):
        uuid = request.data.get('uuid')
        if not uuid:
            return Response({"error": "UUID не предоставлен"}, status=400)

        try:
            progress = PlayerProgress.objects.get(uuid=uuid)
        except PlayerProgress.DoesNotExist:
            return Response({"error": "Question not found"}, status=404)

        return Response({
            "uuid": uuid,
            "level": progress.level.id,
            "points": progress.points,
            "quizPoint": progress.quizPoints,
        })

class GetLevelView(APIView):
    def get(self, request):
        levels = Level.objects.all()
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)

class GetQuestionView(APIView):
    def get(self, request):
        levels = Question.objects.all()
        serializer = QuestionSerializer(levels, many=True)
        return Response(serializer.data)

class GetQuizView(APIView):
    def get(self, request):
        levels = Quiz.objects.all()
        serializer = QuizSerializer(levels, many=True)
        return Response(serializer.data)