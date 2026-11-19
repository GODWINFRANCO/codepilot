from django.db import models

from accounts.models import User

from exams.models import Assesment

# Create your models here.

class Question(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    score = models.PositiveIntegerField()

    assessment = models.ForeignKey(Assesment,on_delete=models.CASCADE)

    sample_input = models.TextField(null=True)

    sample_output = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    question_number = models.PositiveIntegerField(null=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return self.title

    
def save(self, *args, **kwargs):

    last_object = Question.objects.filter(assessment=self.assessment).order_by("question_number").last()

    if last_object:

        self.question_number = last_object.question_number + 1

    else:
        
        self.question_number = 1

    return super().save(*args, **kwargs)
