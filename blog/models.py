from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

status = (
    (0, "Draft"),
    (1, "Published")
)


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=50, null=False,
                            blank=True, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)


class Tag(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=50, null=False, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Tag, self).save(*args, **kwargs)


class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(
        verbose_name="Foto de perfil", upload_to='profile', blank=True)
    bio = models.TextField(max_length=700, blank=True)

    def __str__(self):
        return self.usuario.username

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autor'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Autor.objects.create(usuario=instance)


class Articulo(models.Model):
    nombre = models.CharField(
        max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name='blog_posts')
    contenido = RichTextField(blank=False, null=False)
    cover = models.ImageField(upload_to='blog', blank=True, null=True)
    status = models.IntegerField(choices=status, default=0)
    categorias = models.ManyToManyField(Categoria)
    tags = models.ManyToManyField(Tag)
    is_outstanding = models.BooleanField(default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Articulo, self).save(*args, **kwargs)
