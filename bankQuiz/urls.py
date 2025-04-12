from django.contrib import admin
from django.urls import path, include

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnswerOptionViewSet, StartGameView, GetOptions, GetQuizQuestionView, QuizQuestionViewSet, ResultView, \
    GetLevelView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path

schema_view = get_schema_view(
   openapi.Info(
      title="Название API",
      default_version='v1',
      description="Документация к API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="your@email.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/start_game/<int:pk>/', StartGameView.as_view(), name='start_game'),
    path('api/answer_option/<int:pk>/', GetOptions.as_view(), name='start_game'),
    path('api/quiz-question/<int:pk>/', GetQuizQuestionView.as_view(), name='start_game'),
    path('api/make-answer/', AnswerOptionViewSet.as_view()),
    path('api/make-answer-question/', QuizQuestionViewSet.as_view()),
    path('api/result/', ResultView.as_view()),
    path('get', GetLevelView.as_view(), name='get_options'),
]
