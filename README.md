# Funcionários Flask App
Esta aplicação é um sistema simples de busca de funcionários baseado em Flask. A funcionalidade principal permite que os usuários busquem funcionários por nome e/ou setor. A busca é feita em um banco de dados e os resultados são exibidos em uma página HTML.

## Funcionalidades
Buscar funcionários pelo nome ou setor.
Se apenas um campo for preenchido, a busca será realizada com base nesse critério.
Se os dois campos forem deixados em branco, uma mensagem de erro será exibida.
Os resultados são exibidos em uma página formatada com HTML e CSS.

##Como Funciona
Formulário de busca: O usuário pode preencher o nome e/ou o setor do funcionário para buscar no banco de dados.
Processamento no servidor: Ao enviar o formulário, os dados são processados pela rota /buscar no servidor Flask.
Filtragem de resultados: A consulta é feita no banco de dados filtrando pelo nome e/ou setor.
Exibição dos resultados: Os resultados são renderizados na página resultado.html.

##Exemplo de Fluxo
Se o usuário preencher o campo de nome com "João", a aplicação irá retornar todos os funcionários cujo nome contenha "João".
Se o usuário preencher o campo de setor com "TI", a aplicação retornará todos os funcionários do setor de TI.
Se ambos forem preenchidos, a busca será feita por funcionários que correspondam ao nome "João" e trabalhem no setor "TI".
Caso nenhum campo seja preenchido, uma mensagem de erro será exibida pedindo que o usuário preencha ao menos um campo.

##Estrutura do Projeto

    ├── app.py                 # Arquivo principal da aplicação
    ├── templates/
    │   └── resultado.html      # Template para exibir os resultados da busca
    ├── static/
    │   └── styles.css          # Arquivo CSS para estilização
    └── requirements.txt        # Lista de dependências

## Arquivo app.py
    Este é o arquivo principal que contém a lógica da aplicação.

## Resultados.html
    Este arquivo exibe os resultados da busca.

## Arquivo styles.css
    Este arquivo contém a estilização da página.

## Dependências
    As bibliotecas utilizadas estão listadas no arquivo requirements.txt

# Como rodar:
    Clone o repositório: git clone https://github.com/seuusuario/funcionarios-flask-app.git
## Entre no repositório do projeto 
    cd funcionarios-flask-app
## Instale as dependências: Se estiver usando um ambiente virtual, ative-o primeiro. Em seguida, rode:
    pip install -r requirements.txt
## Execute a aplicação:
    python app.py


    
