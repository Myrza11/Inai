from django.db import models
import uuid

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Level(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Question(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="quizzes")
    question = models.TextField()

    def __str__(self):
        return self.question

class Option(models.Model):
    quiz = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=255)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text} (+{self.points})"

class Quiz(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="quizes")
    question = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.question} "

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    is_correct = models.BooleanField(default=False)


class PlayerProgress(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)  # Используем UUID вместо ID
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    quizPoints = models.IntegerField(default=0)
    finished = models.BooleanField(default=False)

    def get_result(self):
        if self.points >= 6:
            return "🟢 Финансово ответственный"
        elif self.points >= 3:
            return "🟡 Учится на ошибках"
        else:
            return "🔴 Импульсивный решатель"

class Card(models.Model):
    text = models.TextField()