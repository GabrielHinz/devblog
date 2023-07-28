from django import forms

from core.models import Profile, Post, Newsletter


class ProfileForm(forms.ModelForm):
    """
    Formulário para criação ou edição de perfil.

    Este formulário é usado para editar os campos do perfil do usuário.
    Ele adiciona automaticamente a classe 'form-control' a todos os campos,
    garantindo que sejam estilizados corretamente pelo Bootstrap.

    Args:
        *args: Argumentos posicionais adicionais a serem passados para a classe pai.
        **kwargs: Argumentos de palavras-chave adicionais a serem passados para a classe pai.

    Atributos:
        Meta: Classe aninhada que define as meta-informações do formulário.
        - model: Classe Profile
        - fields: Todos os campos do modelo Profile
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = '__all__'


class PostForm(forms.ModelForm):
    """
    Formulário para criação ou edição de perfil.

    Este formulário é usado para criar e editar publicações da aplicação.
    Ele adiciona automaticamente a classe 'form-control' a todos os campos,
    garantindo que sejam estilizados corretamente pelo Bootstrap.

    Args:
        *args: Argumentos posicionais adicionais a serem passados para a classe pai.
        **kwargs: Argumentos de palavras-chave adicionais a serem passados para a classe pai.

    Atributos:
        Meta: Classe aninhada que define as meta-informações do formulário.
        - model: Classe Post
        - fields: Todos os campos do modelo Post
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    """
    Formulário para adicionar novas inscrições.


    Args:
        *args: Argumentos posicionais adicionais a serem passados para a classe pai.
        **kwargs: Argumentos de palavras-chave adicionais a serem passados para a classe pai.

    Atributos:
        Meta: Classe aninhada que define as meta-informações do formulário.
        - model: Classe Newsletter
        - fields: Todos os campos do modelo Newsletter
    """
    class Meta:
        model = Newsletter
        fields = '__all__'
