from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from .models import Articulo, Categoria, Tag
from django.db.models import Q


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
    paginate_by = 4

    def get_queryset(self):
        queryset = Articulo.objects.filter(status=1)
        parameter = self.request.GET.get('search')
        if parameter:
            print(parameter)
            queryset = Articulo.objects.filter(Q(
                categorias__nombre__contains=parameter) | Q(tags__nombre__contains=parameter)).distinct()
            print(queryset)
        return queryset


class PostView(DetailView):
    template_name = 'articulo.html'
    model = Articulo
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'articulo'
