from django import forms

from surveys.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ("answers",)
        widgets = {
            'answers': forms.RadioSelect()
        }
