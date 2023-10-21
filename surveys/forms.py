from django import forms

from surveys.models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("name",)
