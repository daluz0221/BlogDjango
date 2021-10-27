from django.db import models
from django.db.models.expressions import OrderBy
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class PublishManager(models.Manager):
    def get_queryset(self):
        
        return super(PublishManager, self).get_queryset().filter(status='publicado')

class Post(models.Model):
    
    STATUS_CHOICES = (
        ('borrado', 'Borrado'),
        ('publicado', 'Publicado')
    )

    title = models.CharField('Título', max_length=100)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField('Publicado',default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='borrado')


    objects = models.Manager()
    published = PublishManager()


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title