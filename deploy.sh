#!/bin/bash

# Dados da Hospedagem
FILEROOT="/var/devblog/prod"
DOCKER="devblog-prod"
PORT=8000

# Dados da Aplicacao DJANGO
DEBUG=0
SECRET="123456-senha-secreta-do-meu-blog"
HOST="192.168.70.70:8000"

# Criar o diretorio dos arquivos caso nao existam
mkdir -p $FILEROOT/database $FILEROOT/media

# Criar nova imagem do docker
docker build -t $DOCKER:latest . || exit 1

# Remover o docker atual se existir
docker stop $DOCKER &>/dev/null || true
docker rm $DOCKER &>/dev/null || true

# Subir o novo docker com os volumes e as variaveis definidas
docker run -d \
	-v $FILEROOT/database:/www/db \
	-v $FILEROOT/media:/www/media \
	-e BLOGSECRET=$SECRET \
	-e BLOGDEBUG=$DEBUG \
	-e BLOGHOST=$HOST \
	--name $DOCKER \
	-p $PORT:80 \
	$DOCKER:latest

# Executar etapas necessarias da aplicacao
docker exec -i $DOCKER python manage.py makemigrations
docker exec -i $DOCKER python manage.py migrate
docker exec -i $DOCKER python manage.py collectstatic --no-input

# Remover imagens antigas se existirem
docker rmi $(docker images -f "dangling=true" -q) &>/dev/null || true
