"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from core.views import (
    IndexView, PostsView,
    PostDetailView, AboutView,
    ProfileView, PostListView,
    PostAddView, PostEditView,
    PostDeleteView, NewsletterView,
    NewsletterDeleteView, AdminView,
    SetupView, add_newsletter
    )

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('artigos/', PostsView.as_view(), name="posts"),
    path('artigo/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('sobre-mim/', AboutView.as_view(), name="about"),
    path('setup/', SetupView.as_view(), name="setup"),

    path('inscrever/', add_newsletter, name="newsletter"),

    path('admin/', AdminView.as_view(), name="admin"),
    path('admin/perfil/', ProfileView.as_view(), name="admin_perfil"),

    path('admin/newsletter/', NewsletterView.as_view(), name="admin_newsletter"),
    path('admin/newsletter/deletar/<int:pk>/', NewsletterDeleteView.as_view(), name="admin_newsletter_remove"),

    path('admin/posts/', PostListView.as_view(), name="admin_posts"),
    path('admin/posts/adicionar/', PostAddView.as_view(), name="admin_posts_add"),
    path('admin/posts/editar/<int:pk>/', PostEditView.as_view(), name="admin_posts_edit"),
    path('admin/posts/deletar/<int:pk>/', PostDeleteView.as_view(), name="admin_posts_remove"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
