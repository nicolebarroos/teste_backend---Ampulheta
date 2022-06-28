# Teste de Backend - Ampulheta
Este documento tem como objetivo detalhar a avaliação do escopo, das horas de desenvolvimento,
da estimativa dos dias para entrega, das atividades realizadas, tecnologias usadas e instalação e
configuração do projeto.

## Avaliação do escopo
Baseado no cenário detalhado no escopo, julguei necessário arquitetar um projeto Python/Django/Django Rest, 
primeiramente contendo modelos representados pelas entidades, usuários, tempos e projetos, onde:

- Usuários teriam projetos;
- Projetos teriam tempos registrados de trabalho;
- Um usuário tem múltiplos projetos;
- Um projeto tem múltiplos usuários;
- Um projeto tem múltiplos tempos registrados;
- Um tempo registrado só tem um projeto associado;
- Um tempo tem um usuário;

Ao utilizar ModelViewSet nas views, facilitei o uso de grande maioria dos métodos, get, put e post, sem escrita de endpoints.
Serviços que exigiam determinadas regras de negócio, como autenticação, criação de usuário e detalhamento de um tempo baseado
no id de um projeto, julguei necessário escreve-los.
  
Sobreescrevi o método *create_user* para validar a existência de valor no campo "password", no serviço de criação de usuário.
Tornei o ambiente isolado, utilizando Docker para conteinerização, facilitando a chamada do testes automatizados.

Os testes automatizados foram desenvolvidos utilizando Pytest, dessa forma, todos os models, serializers e views foram testados.

##Qualidade de código
- Para ajustes finais visando qualidade de código, usaria Coverage.py que é uma ferramenta popular para medir a cobertura 
de código em aplicativos baseados em Python. Já que usei pytest, realizaria a integração do Coverage.py com pytest via pytest-cov.

- Para verificar em meu código, erros estilísticos ou de programação, usaria a lib Flake8.

Ambos os pontos não foram implementados por conta do tempo. 

## Estimativa de prazo (horas/dias)
Para analizar o prazo do desenvovlimento, utilizei o método de *análise de ponto de funções*, isso significa estimar tempo 
baseado nas funcionalidades detalhadas no escopo. 

- Criação do projeto Ampulheta e da API - *15min*
- Conteinerização em Docker da aplicação - *15min*
- Criação dos modelos e relacionamentos - *1h e 30min*
- Criação dos serializers - *1h*
- Criação dos endpoints de autenticação, criação de usuário e detalhamento do tempo baseado no id de um projeto - *2h*
- Configuração do Pytest - *15min*
- Criação dos testes dos modelos - *1h*
- Criação dos testes dos serializers - *3h*
- Criação dos testes das views - *4h*

Total: 13 horas e 25 min de desenvolvimento, dividios em 4 dias de trabalho.

##Coleção do postman
https://www.getpostman.com/collections/b0090cd9351bb086aeeb

##Instalação e configuração do projeto
Para rodar o container:

> sudo docker-compose -f docker-compose.yml up --build

ou

> docker-compose up -d --build

Para xecutar os testes:

> sudo docker-compose -f docker-compose.yml exec -T api  pytest -s -v --traceconfig 

ou

> docker-compose exec movies pytest