from django.shortcuts import render
from django.views.generic import TemplateView


def shab_func(request):
    return render(request, 'second_task/class_template.html')


class ShabClass(TemplateView):
    template_name = 'second_task/func_template.html'

