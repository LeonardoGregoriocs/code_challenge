# Code Challenge

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local.

  ####  Realize o clone do projeto:
    https://gitlab.com/Leonardogregoriocs/digital_republic_code_challenge.git

### 📋 Pré-requisitos & Instalação

### Existem 2 maneiras para rodarmos o projeto, para isso vou separar em duas partes os pré-requisitos.

### Parte 1:

   Instale o [Python 3.10](https://www.python.org/downloads)

   Instale o [Pip](https://pypi.org/project/pip/)

Após a instalação do Python e do Pip, rode os seguintes comandos:

      - pip install -r requirements.txt   - Para instalarmos as dependências do projeto.

      - uvicorn app.main:app --reload    - Para iniciliarmos o projeto.

Após esses dois comandos, o projeto já estará rodando na porta http://127.0.0.1:8000.

Você pode acessar a documentação no [SWAGGER](http://127.0.0.1:8000/docs)

### Parte 2:
   Instalar o [docker](https://docs.docker.com/get-docker)

Após realizar a instalação do docker, basta rodar os comandos abaixo:

      - docker-compose up --build -d

Após rodar esse comando, o projeto já estará rodando na porta http://127.0.0.1:8004.

Você pode acessar a documentação no [SWAGGER](http://127.0.0.1:8004/docs)


#### Para rodar os testes unitários, basta rodar os comandos abaixo:

      pytest

      pytest --cov-config=.coveragerc -vv --cov=. --cov-report=term-missing

#### Exemplo de entrada de dados:

    {
      "measurements": [
        {
          "wall_height": 5.0,
          "wall_length": 3.0,
          "amount_of_doors": 0,
          "amount_of_windows": 0
        },
        {
          "wall_height": 5.0,
          "wall_length": 3.0,
          "amount_of_doors": 0,
          "amount_of_windows": 0
        },
        {
          "wall_height": 5.0,
          "wall_length": 3.0,
          "amount_of_doors": 0,
          "amount_of_windows": 0
        },
        {
          "wall_height": 5.0,
          "wall_length": 3.0,
          "amount_of_doors": 10,
          "amount_of_windows": 0
        }
      ]
    }

#### Exemplo de saída de dados:
      {
        'Total Measuarements': 60.0,
        'Gallon 0.5': 4.0,
        'Gallon 18': 0,
        'Gallon 2.5': 0,
        'Gallon 3.6': 3
      }
