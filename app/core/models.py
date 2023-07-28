from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Profile(models.Model):
    """
    Modelo que representa um perfil de usuário.
    
    Campos:
        - name (CharField): O nome do perfil.
        - profile_picture (ImageField): A foto de perfil do usuário.
        - about_me (TextField): Uma descrição sobre o usuário.
        - linkedin (URLField): A URL do perfil do usuário no LinkedIn.
        - github (URLField): A URL do perfil do usuário no GitHub.
        - instagram (URLField): A URL do perfil do usuário no Instagram.
        - twitter (URLField): A URL do perfil do usuário no Twitter.
        - blog_name (CharField): O nome do blog do usuário.
        - blog_description (TextField): Uma descrição do blog do usuário.
        - blog_theme (CharField): a cor do tema do blog.
    """
    THEME_CHOICES = [
        ('#ff5e3a', 'Laranja'),
        ('#4caf50', 'Verde'),
        ('#9c27b0', 'Roxo'),
        ('#ff9800', 'Amarelo'),
        ('#2196f3', 'Azul'),
        ('#e91e63', 'Rosa'),
        ('#00bcd4', 'Ciano'),
        ('#8bc34a', 'Verde Claro'),
        ('#ffc107', 'Amarelo Escuro'),
        ('#3f51b5', 'Azul Escuro'),
    ]
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile/')
    about_me = models.TextField()
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    blog_name = models.CharField(max_length=100)
    blog_description = models.TextField()
    blog_theme = models.CharField(max_length=10, choices=THEME_CHOICES)
    
    def __str__(self):
        return self.name
    
   
class Newsletter(models.Model):
    """
    Modelo que representa uma inscrição em uma newsletter.
    
    Campos:
        - email (EmailField): O endereço de e-mail da inscrição.
        - subscribed_at (DateTimeField): A data e hora em que a inscrição foi feita.
    """
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email


class Post(models.Model):
    """
    Representa um post no blog.

    Campos:
        - title (str): O título do post.
        - banner (ImageField): O banner do post.
        - description (str): A descrição do post.
        - content (RichTextField): O conteúdo completo do post.
        - created (DateTimeField): A data e hora de criação do post.
    """
    title = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='posts', null=True, blank=True)
    description = models.TextField()
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
