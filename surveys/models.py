from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Survey(models.Model):
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="categories"
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    answers = models.ManyToManyField("Answer")
    correct_answer = models.ForeignKey("Answer", on_delete=models.CASCADE, related_name="correct_answer")
    used = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.answer}"
