from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created')
    up_date = models.DateTimeField('date updated', default=timezone.now)

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct_choice = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text