from random import choices
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    
    POST_STATUS = (
        ('active', 'ativo'),
        ('draft', 'Rascunho'),
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    #slug = models.SlugField(unique=True, null=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True) #ao adicionar o post é criada uma data no banco.
    updated_at = models.DateField(auto_now=True) # sempre que o post/item for salvo a data é atualizada automáticamente.
    status = models.CharField(max_length=15, choices=POST_STATUS)



def __str__(self):
    return self.title        
