from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import SignUpForm


class Login1View(LoginView):
    template_name = 'login.html'


class PassResetView(PasswordResetView):
    template_name = 'pass_reset.html'
    email_template_name = 'pass_reset_email.html'
    subject_template_name = 'pass_reset_subject.txt'
    success_url = reverse_lazy('accounts:pass_reset_done')


class PassResetDoneView(PasswordResetDoneView):
    template_name = 'pass_reset_done.html'


class PassConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:pass_complete')
    template_name = 'pass_confirm.html'


class PassCompleteView(PasswordResetCompleteView):
    template_name = 'pass_complete.html'


class PassChangeView(PasswordChangeView):
    success_url = reverse_lazy('accounts:pass_change_done')
    template_name = 'pass_change.html'


class PassChangeDoneView(PasswordChangeDoneView):
    template_name = 'pass_change_done.html'


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



