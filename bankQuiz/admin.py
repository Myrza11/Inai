from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Level)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(Question)
admin.site.register(Option)