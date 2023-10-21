from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import SignUpForm


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('surveys:survey_list')
    template_name = 'users/signup.html'
