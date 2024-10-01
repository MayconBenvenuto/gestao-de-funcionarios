# Projeto de Consulta de Funcionários

Este projeto é uma aplicação web que permite buscar funcionários em um banco de dados com base em seu nome ou setor. A aplicação é construída usando **Flask** e **SQLAlchemy** para o backend e **HTML/CSS** para a interface de usuário.

## Funcionalidades

- Consulta de funcionários por nome.
- Consulta de funcionários por setor.
- Retorno de resultados com base em filtros aplicados (nome, setor ou ambos).
- Exibe uma mensagem quando nenhum filtro é aplicado, evitando retorno de todos os funcionários.

## Tecnologias Utilizadas

- **Python 3.x**
- **Flask** (Framework Web)
- **SQLAlchemy** (ORM para interação com banco de dados)
- **HTML/CSS** (Interface de usuário)
- **Jinja2** (Template engine do Flask)

## Requisitos

Antes de iniciar o projeto, você precisa ter instalado:

- [Python 3.x](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installation/) para gerenciar as dependências do projeto
- Um banco de dados compatível com SQLAlchemy (como SQLite ou PostgreSQL)

## Instalação

1. Clone este repositório:
    ```
   git clone https://github.com/MayconBenvenuto/gestao-de-funcionarios.git
    
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   
3. Configure o banco de dados:
  ```
  Modifique o arquivo config.py para incluir as informações do seu banco de dados.
  Crie o banco de dados e execute as migrações (se aplicável).
