from django import template
from ..models import Articulo, Categoria, Tag

register = template.Library()
@register .simple_tag
def get_latest_three():
    latest = Articulo.objects.all()[:3]
    return latest


@register .simple_tag
def get_categories():
    categorias = Categoria.objects.all()
    categorias_dic = {}
    for categoria in categorias:
        id = categoria.id
        if Articulo.objects.filter(categorias__id=id):
            categorias_dic[categoria.nombre] = Articulo.objects.filter(
                categorias__id=id).count()
    return categorias_dic


@register .simple_tag
def get_tags():
    tags = Tag.objects.all()
    return tags
