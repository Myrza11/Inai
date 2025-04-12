from rest_framework import serializers
from .models import Level, Question, Option, PlayerProgress, Quiz


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'points']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question', 'options']

class LevelSerializer(serializers.ModelSerializer):
    quizzes = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Level
        fields = ['id', 'title', 'quizzes']

class PlayerProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProgress
        fields = ['id', 'user', 'level', 'points', 'finished']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"