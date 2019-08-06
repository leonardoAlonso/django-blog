from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.
from .models import Articulo


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['destacados'] = Articulo.objects.filter(is_outstanding=True)
        context['latest'] = Articulo.objects.all()[:3]
        return context


class BlogView(ListView):
    template_name = 'blog.html'
    context_object_name = 'articulos'
    queryset = Articulo.objects.filter(status=1)
    paginate_by = 4
