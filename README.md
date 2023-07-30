# Blog de Desenvolvedor em Python

Este é um blog desenvolvido em Python usando o framework Django. O objetivo deste projeto é compartilhar conhecimentos e experiências sobre programação com a comunidade Python. Sinta-se à vontade para contribuir e aprender!

Este blog foi utilizado como o código principal da live de Implantação Contínua: Git, Pipelines CI/CD e Docker
* Live: https://www.youtube.com/watch?v=2UCjzofKpXk

## Requisitos
Antes de rodar o projeto, certifique-se de ter os seguintes requisitos instalados em seu sistema:

- Docker
- Git
- Jenkins (opcional)
- Python 3.8 (com o virtualenv instalado)

## Configuração Padrão

1. Configure o script deploy.sh
* Modifique as variáveis de acordo com sua necessidade
* Altere a senha de aplicativo e o host utilizado

2. Utilize o script de deploy

  ```shell
  ./deploy.sh
  ```
   **Nota:** Utilize este script com o usuário root

2. Verifique o container

  ```shell
  sudo docker ps
  ```

 **Nota:** O projeto estará disponível em http://_seu host_:_sua porta_
 * ex: http://localhost:8000
   
## Configuração (Sem Docker)

1. Clone o repositório

  ```shell
  git clone https://github.com/GabrielHinz/devblog.git
  cd devblog
  ```
   
2. Crie um ambiente virtual e ative-o:

  ```shell
  python3.8 -m venv venv
  source venv/bin/activate
  ```

3. Instale as dependências:

  ```shell
  pip install -r app/requirements.txt
  ``` 
  
4. Realize as migrações para o seu banco de dados:

  ```shell
  python manage.py migrate
  ``` 

5. Rode o aplicativo DJANGO

  ```shell
  cd app
  python manage.py runserver
  ``` 

O projeto estará disponível em http://localhost:8000/.

 **Nota:** Esta aplicação foi montada para ser rodada em um container Docker
  
## Contribuição
* Sinta-se livre para contribuir com este projeto
* Crie seu pull request, e estaremos revisando e implementando seu código.

## Autores
- **Gabriel Hinz** - *Eng. Devops* -
    [Sobre](https://gabriel.legendproject.com.br/)
    
## Licença
Este projeto está licenciado sob a licença MIT (LICENSE.md)
