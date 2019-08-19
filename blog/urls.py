from django.urls import path, include
from .views import HomeView, BlogView, PostView, CategoriaView, TagView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog', BlogView.as_view(), name='blog'),
    path('blog/articulo/<slug:slug>',
         PostView.as_view(), name="articulo"),
    path('blog/categoria/<slug:slug>',
         CategoriaView.as_view(), name="categoria"),
    path('blog/tag/<slug:slug>',
         TagView.as_view(), name="tag")
]
