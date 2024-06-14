# Prova 2 do Módulo 10 - Felipe Campos

## Explicação

### Organização das pastas

```
.
├── docker-compose.yaml
├── gateway
│   └── nginx.conf
├── Insomnia.json
├── logs-volumes
│   ├── app.log
│   ├── app.log.2024-06-14_13-08
│   ├── app.log.2024-06-14_13-31
│   └── app.log.2024-06-14_13-40
├── README.md
└── src
    ├── database
    │   ├── database.py
    │   ├── models.py
    │   └── schemas.py
    ├── Dockerfile
    ├── logging_config.py
    ├── main.py
    ├── ref.py
    └── requirements.txt
```

- A pasta src contém todos os códigos da aplicação, sendo composta por um Dockerfile para criar a imagem do Back-End, main.py, o arquivo de execução principal, requirements.txt para instalar as depedências e o diretório database, onde se encontram os modelos e esquemas para estruturam o banco de dados.
- collection_insomnia.json contém a documentação da API
- docker-compose.yaml: lança os containers da aplicação
- logs-volumes: armazena os logs da aplicação
- gateway: armazena a a confirguração do gateway feito em nginx

### Rotas 

Nesta prova foi proposto que os alunos criassem um Back-End de uma aplicação, com rotas a fim de realizar o CRUD de um post. Para isso foram desenvolvidas 5 rotas, elas são:

- **GET**: /blog
- **GET**: /blog/id 
- **POST** /blog
- **PUT**: /blog/id
- **DELETE**: /blog/id

Essas rotas, respectivamente, pegam todos os posts do blog, pegam um post apenas, adiciona um novo post, atualiza um post e remove um post.

### Dockerização

Também foi solicitado que os alunos dockerizassem suas soluções. Dado isso, um docker-compose foi criado, que lança dois containers, um do Back-End e outro do Banco de Dados. Para armazenar as informações, foi utilizado Postgres, a partir de uma imagem puxada no próprio docker-compose. Além disso, uma imagem é criada para dar suporte ao container do Back-End, uma vez que é necessário baixar diversas depedências a fim de executar o a aplicação.

### Gateway

Foi adicionado um gateway ao projeto na porta 8001, que redireciona todos o pedidos para a porta 8000, onde está rodando o backend da aplicação

### Logs

Também foi adicionado um sistema de logs e, como pedido, apenas são registrados eventos mais críticos, como erros e avisos. Esses dados são salvos no logs-volumes, onde é possível acompanhar os eventos que ocorreram na aplicação.

## Como rodar

Primeiro é necessário clonar o repositório para facilitar a execução:

```
git clone https://github.com/FelipeCampos14/p2-modulo10.git
```

Após isso, basta rodar o docker-compose que ele irá lançar os containers da aplicação:

```
docker compose up --build
```
