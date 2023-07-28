from django.views.generic import (
    TemplateView, ListView, 
    FormView, CreateView, 
    UpdateView, DeleteView,
    DetailView,
)
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models.functions import TruncMonth
from django.db.models import Count

from core.forms import ProfileForm, PostForm, NewsletterForm
from core.models import Profile, Post, Newsletter


class IndexView(ListView):
    """
    Classe IndexView
    ----------------
    Classe responsável por exibir a página inicial (index) da aplicação.
    Herda da classe ListView do Django para renderizar um template simples.
    Por padrão, o template esperado é "index.html".
    
    Atributos:
        - template_name: nome do template a ser renderizado (padrão: "index.html")
        - model: nome do modelo que vai ser listado
        - context_object_name: nome que será enviado para o template contendo os posts
        - paginate_by: quantidade de posts para serem exibidos por página
    Métodos:
        - get_context_data(): retorna o contexto de dados para ser usado no template
    """
    template_name = "pages/index.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 4
    
    def get(self, request, *args, **kwargs):
        if Profile.objects.filter(pk=1).exists():
            return super().get(request, *args, **kwargs)
        return redirect("/setup")

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(pk=1)
        context = super().get_context_data(**kwargs)
        context["title"] = "Página Inicial"
        context["menu"] = "index"
        context["profile"] = profile
        return context
    

class PostsView(ListView):
    template_name = "pages/articles.html"
    model = Post
    ordering = "created"
    context_object_name = "posts"
    paginate_by = 9
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.reverse()
    
    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(pk=1)
        context = super().get_context_data(**kwargs)
        context["title"] = "Artigos"
        context["menu"] = "posts"
        context["profile"] = profile
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "pages/post.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(pk=1)
        context = super().get_context_data(**kwargs)
        context["title"] = context["post"].title
        context["profile"] = profile
        return context


class AboutView(TemplateView):
    template_name = "pages/about.html"
    
    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(pk=1)
        context = super().get_context_data(**kwargs)
        context["title"] = "Sobre"
        context["profile"] = profile
        context["menu"] = "about"
        return context


# Admin
class ProfileView(LoginRequiredMixin, FormView):
    form_class = ProfileForm
    login_url = "/"
    template_name = "pages/admin/profile.html"
    success_url = "/admin/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = "profile"
        context["profile"] = Profile.objects.get(id=1)
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        profile = Profile.objects.get(id=1)
        kwargs['instance'] = profile
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class NewsletterView(LoginRequiredMixin, ListView):
    template_name = "pages/admin/newsletter.html"
    login_url = "/"
    model = Newsletter
    context_object_name = "emails"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = "newsletter"
        context["profile"] = Profile.objects.get(id=1)
        return context
    

class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    login_url = "/"
    template_name = 'pages/admin/index.html'
    success_url = reverse_lazy('admin_newsletter')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = "newsletter"
        context["profile"] = Profile.objects.get(id=1)
        return context


class PostListView(LoginRequiredMixin, ListView):
    template_name = "pages/admin/posts-list.html"
    login_url = "/"
    model = Post
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = "posts"
        context["profile"] = Profile.objects.get(id=1)
        return context


class PostAddView(LoginRequiredMixin, CreateView):
    template_name = "pages/admin/posts-form.html"
    login_url = "/"
    form_class = PostForm
    model = Post
    success_url = reverse_lazy("admin_posts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = "posts"
        context["profile"] = Profile.objects.get(id=1)
        return context
    

class PostEditView(LoginRequiredMixin, UpdateView):
    template_name = "pages/admin/posts-form.html"
    login_url = "/"
    form_class = PostForm
    model = Post
    success_url = reverse_lazy("admin_posts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = "posts"
        context["profile"] = Profile.objects.get(id=1)
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    login_url = "/"
    template_name = 'pages/admin/index.html'
    success_url = reverse_lazy('admin_posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = "posts"
        context["profile"] = Profile.objects.get(id=1)
        return context


class AdminView(LoginRequiredMixin, TemplateView):
    template_name = "pages/admin/index.html"
    login_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Dados de publicações
        posts = Post.objects.annotate(month=TruncMonth('created')).values(
            'month').annotate(count=Count('id')).order_by('month')
        labels = [post['month'].strftime('%B %Y') for post in posts]
        data = [post['count'] for post in posts]

        # Dados de Inscrições
        subscribes = Newsletter.objects.annotate(month=TruncMonth('subscribed_at')).values(
            'month').annotate(count=Count('id')).order_by('month')
        sublabels = [subs['month'].strftime('%B %Y') for subs in subscribes]
        subdata = [subs['count'] for subs in posts]

        context["subtotal"] = Newsletter.objects.count()
        context["posttotal"] = Post.objects.count()
        context["labelschart"] = labels
        context["datachart"] = data
        context["sublabels"] = sublabels
        context["subdata"] = subdata
        context["menu"] = "home"
        context["profile"] = Profile.objects.get(id=1)
        return context
    

# Setup
class SetupView(TemplateView):
    """
    Classe SetupView
    ----------------
    Classe responsável por exibir a página de setup da aplicação.
    Herda da classe TemplateView do Django para renderizar um template simples.
    Por padrão, o template esperado é "setup.html".
    
    Atributos:
        - template_name: nome do template a ser renderizado (padrão: "setup.html")
    Métodos:
        - get(): recebe e retorna os dados requisição do tipo GET
        - post(): recebe a requisição POST e realiza as operações de setup.
        - get_context_data(): retorna o contexto de dados para ser usado no template
    """
    template_name = "pages/setup.html"

    def get(self, request, *args, **kwargs):
        if Profile.objects.filter(pk=1).exists():
            return redirect("/")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        profileform = ProfileForm(request.POST or None, request.FILES or None)
        userform = UserCreationForm({
            "username": request.POST["username"],
            "password1": request.POST["password1"],
            "password2": request.POST["password1"],
        })
        if all([profileform.is_valid(), userform.is_valid()]):
            profileform.save()
            userform.save()
            username = userform.cleaned_data.get('username')
            password = userform.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            errors = []
            errors.append(profileform.errors)
            errors.append(userform.errors)
        return render(request, self.template_name, 
                      {'userform': userform, 'profileform': profileform, 'errors': errors})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profileform'] = ProfileForm()
        context['postform'] = PostForm()
        return context


# Newsletter
def add_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewsletterForm()

    return redirect('index')
