# A Monitoria - API de Ofertas

<a href="https://2019-2-arquitetura-desenho.github.io/wiki/" target="_blank"><img src="https://img.shields.io/badge/A%20Monitoria-2019.2-purple.svg"></a> <a href="https://2019-2-arquitetura-desenho.github.io/wiki/#equipe" target="_blank"> <img src="https://img.shields.io/badge/Grupo-05-blue.svg" alt="Grupo 05"></a> <a href="https://heroku-badge.herokuapp.com/?app=amonitoria-offers" target="_blank"><img src="https://heroku-badge.herokuapp.com/?app=amonitoria-offers"></a>

Repositório destinado à disciplina de Desenho e Arquitetura de Software (2019.2). Reserva-se a disponibilizar uma API para fornecer as disciplinas do campus UnB-Gama ofertadas pelo Matrícula Web da Universidade de Brasília.

- Oferta completa:
  - [http://amonitoria-offers.herokuapp.com/discipline/](http://amonitoria-offers.herokuapp.com/discipline/)
- Oferta de disciplina pelo código:
  - [http://amonitoria-offers.herokuapp.com/discipline/?code=103667](http://amonitoria-offers.herokuapp.com/discipline/?code=103667)

# Rode com Docker

Para executar localmente a aplicação, proceda com os seguintes passos:

1. Instale o Docker [neste link](https://docs.docker.com/install/linux/docker-ce/ubuntu/).
2. Na pasta principal do projeto, inicie o docker com o comando: `make start-docker`.
3. Rode localmente: `make server`.

Deploy: realizado através do Heroku.
