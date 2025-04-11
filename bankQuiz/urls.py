from django.contrib import admin
from django.urls import path, include

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnswerOptionViewSet, StartGameView, GetOptions, GetQuizQuestionView, QuizQuestionViewSet, ResultView

urlpatterns = [
    path('api/start_game/<int:pk>/', StartGameView.as_view(), name='start_game'),
    path('api/answer_option/<int:pk>/', GetOptions.as_view(), name='start_game'),
    path('api/quiz-question/<int:pk>/', GetQuizQuestionView.as_view(), name='start_game'),
    path('api/make-answer/', AnswerOptionViewSet.as_view()),
    path('api/make-answer-question/', QuizQuestionViewSet.as_view()),
    path('api/result/', ResultView.as_view())
]
