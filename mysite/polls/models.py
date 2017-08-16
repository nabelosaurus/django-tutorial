from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    # class Meta:
    #     verbose_name = "Question"
    #     verbose_name_plural = "Questions"

    # def __str__(self):
    #     pass
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # class Meta:
    #     verbose_name = "Choice"
    #     verbose_name_plural = "Choices"

    # def __str__(self):
    #     pass