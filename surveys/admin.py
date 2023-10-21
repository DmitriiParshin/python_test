from django.contrib import admin

from surveys.models import Survey, Category, Question, Answer, UserAnswer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'survey')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'correct_answer', 'category')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', )
