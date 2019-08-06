from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from .models import Articulo


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['destacados'] = Articulo.objects.filter(is_outstanding=True)
        print(context)
        return context
