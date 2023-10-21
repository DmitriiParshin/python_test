from django.contrib import admin

from surveys.models import Survey, Category, Question, Answer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'survey')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'used', 'category')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'question', 'user')
