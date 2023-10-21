from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from surveys.forms import AnswerForm
from surveys.models import Survey, Question


@login_required
def survey_list(request):
    survey_objs = Survey.objects.all()
    context = {
        "surveys": survey_objs,
    }
    return render(request, 'surveys/survey_list.html', context)


@login_required
def survey_process(request, survey_id):
    survey_obj = Survey.objects.filter(id=survey_id).first()
    if not survey_obj:
        return redirect('surveys:survey_list')
    category_objs = survey_obj.categories.all()
    question_obj = Question.objects.filter(category__in=category_objs, used=False).order_by("id").first()
    if not question_obj:
        return redirect('surveys:survey_finished')
    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            answer_obj = form.save(commit=False)
            answer_obj.question = question_obj
            answer_obj.user = request.user
            answer_obj.save()
            question_obj.used = True
            question_obj.save()
        return redirect('surveys:survey_process', survey_obj.id)
    context = {
        "form": form,
        "question": question_obj,
    }
    return render(request, 'surveys/survey_process.html', context)


@login_required
def survey_finished(request):
    return redirect("surveys:survey_list")
