# Generated by Django 4.2.20 on 2025-04-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bankQuiz", "0003_remove_playerprogress_anonymous_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="playerprogress",
            name="quizPoints",
            field=models.IntegerField(default=0),
        ),
    ]
