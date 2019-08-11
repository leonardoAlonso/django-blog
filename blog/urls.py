from django.urls import path, include
from .views import HomeView, BlogView, PostView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog', BlogView.as_view(), name='blog'),
    path('blog/articulo/<slug:slug>',
         PostView.as_view(), name="articulo")
]
