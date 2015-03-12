import datetime
from django.db import models
from django.utils import timezone

class QuestionType(models.Model):
    question_type_text = models.CharField(max_length=200)
    other_stuff = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.question_type_text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_type = models.ForeignKey(QuestionType)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
