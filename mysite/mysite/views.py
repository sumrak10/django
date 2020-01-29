from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from mysite.models import Profile
from mysite.forms import ProfileForm, RegisterForm

from django.http import JsonResponse
import serial

class homeView(TemplateView):
	template_name = "homePage.html"

class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                self.create_new_user(form)
                messages.success(request, "Вы успешно зарегистрировались!")
                return redirect(reverse("login"))

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def create_new_user(self, form):
        email = None
        if 'email' in form.cleaned_data:
            email = form.cleaned_data['email']
        User.objects.create_user(form.cleaned_data['username'], email, form.cleaned_data['password'],
                                 first_name=form.cleaned_data['first_name'],
                                 last_name=form.cleaned_data['last_name'])

class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class ProfileView(TemplateView):
    template_name = "registration/profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not Profile.objects.filter(user=request.user).exists():
            return redirect(reverse("edit_profile"))
        context = {
            'selected_user': request.user
        }
        return render(request, self.template_name, context)

class EditProfileView(TemplateView):
    template_name = "registration/edit_profile.html"

    def dispatch(self, request, *args, **kwargs):
        form = ProfileForm(instance=self.get_profile(request.user))
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=self.get_profile(request.user))
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request, "Профиль успешно обновлен!")
                return redirect(reverse("profile"))
        return render(request, self.template_name, {'form': form})

    def get_profile(self, user):
        try:
            return user.profile
        except:
            return None

# def send_data_on_COM():
# 	if request.method == 'GET':
#         data = ' method GET'
#     elif request.method == 'POST':
#         data = ' method POST'
#     else:
#         data = ''
#     a = {'Hello world': data}
#     response = JsonResponse(data)
#     response['Access-Control-Allow-Origin'] = '*'
#     return response











"""пересадить manage в отдельное приложение
и сделать чтобы подсветка управлялась с питон скрипта 
(библиотека сериал подробнее прочитай в гугле но сначала сделай 
чтобы просто по нажатии на кнопку исполнялся питон скрипт)"""