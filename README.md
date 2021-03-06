# Central de Erros - Oh My Log

Projeto final realizado para a plataforma da Codenation no **Acelera Dev - Python**, apoiado pela Stone.

## Índice

- [Central de Erros - Oh My Log](#central-de-erros---oh-my-log)
  - [Índice](#índice)
  - [1. Sobre o projeto](#1-sobre-o-projeto)
    - [1.1 Informações cedidas pela Codenation para realização do projeto](#11-informações-cedidas-pela-codenation-para-realização-do-projeto)
      - [1.1.1 Contexto](#111-contexto)
      - [1.1.2 Objetivo](#112-objetivo)
    - [1.2. Wireframes](#12-wireframes)
      - [1.2.1 Cadastro](#121-cadastro)
      - [1.2.2 Login](#122-login)
      - [1.2.3 Dashboard](#123-dashboard)
      - [1.2.4 Ambientes](#124-ambientes)
      - [1.2.5 Ordenação](#125-ordenação)
      - [1.2.6 Filtro](#126-filtro)
      - [1.2.7 Detalhes do erro](#127-detalhes-do-erro)
    - [1.2 Prazo](#12-prazo)
  - [2. Mão na massa](#2-mão-na-massa)
    - [2.3 Ferramentas utilizadas](#23-ferramentas-utilizadas)
    - [2.2 Dependências](#22-dependências)
  - [3. Estado atual do projeto:](#3-estado-atual-do-projeto)
    - [20/07/2020 - Pausado por um tempo](#20072020---pausado-por-um-tempo)
    - [24/07/2020 - Retornando](#24072020---retornando)

## 1. Sobre o projeto

---

### 1.1 Informações cedidas pela Codenation para realização do projeto

#### 1.1.1 Contexto

Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação (backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante que os desenvolvedores possam centralizar todos os registros de erros em um local, de onde podem monitorar e tomar decisões mais acertadas. Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações.

#### 1.1.2 Objetivo

Como o programa (ou aceleração) possui ênfase no backend, o objetivo principal é:

- Criar endpoints para serem usados pelo frontend da aplicação;
- Criar um endpoint que será usado para gravar os logs de erro em um banco de dados relacional;
- A API deve ser segura, permitindo acesso apenas com um token de autenticação válido;

Porém, a implementação do frontend (não obrigatória) também pode ocorrer nos seguintes moldes:

- Deve implementar as funcionalidades apresentadas nos wireframes;
- Deve ser acessada adequadamente tanto por navegadores desktop quanto mobile;
- Deve consumir a API do produto;
- Desenvolvida na forma de uma Single Page Application;

### 1.2. Wireframes

#### 1.2.1 Cadastro

<img src="https://codenation-challenges.s3-us-west-1.amazonaws.com/central-erros/1-cadastro.png"
     alt="Tela de cadastro"
     style="float: left; margin-right: 10px;" />

#### 1.2.2 Login

<img src="https://codenation-challenges.s3-us-west-1.amazonaws.com/central-erros/2-login.png"
     alt="Tela de login"
     style="float: left; margin-right: 10px;" />

#### 1.2.3 Dashboard

<img src="https://codenation-challenges.s3-us-west-1.amazonaws.com/central-erros/3-dashboard.png"
     alt="Dashboard"
     style="float: left; margin-right: 10px;" />

#### 1.2.4 Ambientes

<img src="https://codenation-challenges.s3-us-west-1.amazonaws.com/central-erros/4-ambientes.png"
     alt="Ambientes"
     style="float: left; margin-right: 10px;" />

#### 1.2.5 Ordenação

<img src="https://codenation-challenges.s3-us-west-1.amazonaws.com/central-erros/5-order.png"
     alt="Ordenação"
     style="float: left; margin-right: 10px;" />

#### 1.2.6 Filtro

<img src="https://codenation-challenges.s3-us-west-1.amazonaws.com/central-erros/6-filtro.png"
     alt="Filtro"
     style="float: left; margin-right: 10px;" />

#### 1.2.7 Detalhes do erro

<img src="https://codenation-challenges.s3-us-west-1.amazonaws.com/central-erros/7-detalhes.png"
     alt="Detalhes do erro"
     style="float: left; margin-right: 10px;" />

### 1.2 Prazo

O projeto deverá ser entregue até o dia 20/07/2020, juntamente com um vídeo de explicação/apresentação do realizado pelo participante.

## 2. Mão na massa

---

### 2.3 Ferramentas utilizadas

- [Visual Studio Code](https://code.visualstudio.com/)

### 2.2 Dependências

Para testar o projeto em sua máquina, é necessário seguir os seguintes passos:

- Instalar a biblioteca **virtualenv** globalmente para criar um virtual environment:

```bash
pip3 install virtualenv
```

- Criar um novo virtual environment:

```bash
cd venv
python -m venv .
```

- Ativar o virtual environment para execução:

```bash
cd ..
source venv/bin/activate
```

- Instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

## 3. Estado atual do projeto:

### 20/07/2020 - Pausado por um tempo

Decidi pausar o desenvolvimento desse projeto pois não estava me dando bem com as libs de URL do Django REST, chegando até mesmo a cortar dois Models (quase 3) para simplificar a URL (/machine/id/application/id/execution/id/event/id) devido a perder muito tempo configurando e tentando entender os lookups, filters, etc. Quando cheguei perto, o tempo já estava no limite (infelizmente).

Dificuldades encontradas até aqui e "superações":
- **Decidir entre Flat VS Nested URL** _(/machine?application_id vs /machine/id/application/id..)_.: Quase superada, pois travei ao seguir pelo caminho das URLs aninhadas ao utilizar implementações via libs do Django Rest Framework. O erro fatal foram configurações específicas nas quais 1 recurso filho não deveria aparecer em outro recurso-pai que não o possuísse.
- **Definir um padrão a seguir na API:**: Superada ao tentar utilizar as especificações do [JSON:API](https://jsonapi.org/).
- **Criação de filtros fora das classes padrões do Django:** Não realizado.
- **Entender o ecossistema Django e seu funcionamento:** Ganhei uma boa noção, porém, ainda faltam vários tópicos para ter um entendimento melhor do assunto.
- **Workflow no Git:** ainda faço uns commits que poderiam ser melhores (no quisito texto, necessidade, etc), mas foi uma experiência muito boa!

**Planos pro futuro**
- Terminar a parte da URL.
- Criar os filtros.
- Criar wireframes melhores.
- Fazer um prótipo de telas.
- Colocar "no ar" a API.
- Criar a parte de Front-end.
- Juntar tudo e ter a aplicação completa.

### 24/07/2020 - Retornando

Após algumas pesquisas, decidi retornar aos poucos com o desenvolvimento do projeto, visto que, em teoria, falta pouco para se tornar uma aplicação completa (ainda que eu termine após o prazo estipulado).
