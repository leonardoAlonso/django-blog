from django.contrib import admin
from .models import Categoria, Tag, Autor, Articulo
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Autor)
admin.site.register(Articulo)
