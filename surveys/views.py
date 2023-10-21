from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from surveys.forms import QuestionForm
from surveys.models import Survey, Question, Answer, UserAnswer


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
    question_obj = Question.objects.filter(
        category__in=category_objs, used=False
    ).order_by("id").first()
    if not question_obj:
        return redirect('surveys:survey_finished')
    answer_objs = question_obj.answers
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST or None)
        print(form.errors)
        print(":LJK:LKJ:LKJ++++++++++")
        if form.is_valid():
            print(form.errors, ";LKL:K:890")
            print(":LJK:LKJ:LKJ")
            answer_id = request.POST.get('answer')
            answer = Answer.objects.filter(id=answer_id).first()
            UserAnswer.objects.create(
                user=request.user, question=question_obj, answer=answer
            )
            question = form.save(commit=False)
            question.used = True
            question.save()

        return redirect('surveys:survey_process', survey_obj.id)
    context = {
        "form": form,
        "question": question_obj,
        "answers": answer_objs
    }
    return render(request, 'surveys/survey_process.html', context)


@login_required
def survey_finished(request):
    return redirect("surveys:survey_list")
