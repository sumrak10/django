from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

class homeView(TemplateView):
	template_name = "homePage.html"