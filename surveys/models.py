from django.db import models


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
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="questions"
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    name = models.CharField(max_length=128)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
