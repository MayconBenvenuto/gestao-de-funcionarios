from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Carregar as variáveis do .env
load_dotenv()

app = Flask(__name__)

# Configurações do banco de dados
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo da tabela funcionarios
class Funcionario(db.Model):
    __tablename__ = 'funcionarios'  # O nome da tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Numeric(10, 2), nullable=False)
    departamento = db.Column(db.String(50), nullable=False)
    loja = db.Column(db.String(50), nullable=False)
    data_contratacao = db.Column(db.Date, nullable=False)
    data_demissao = db.Column(db.Date, nullable=True)  # A demissão é opcional

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    nome = request.form.get('nome', '').strip()
    setor = request.form.get('setor', '').strip()

    query = Funcionario.query

    if nome:
        query = query.filter(Funcionario.nome.ilike(f'%{nome}%'))  
    if setor:
        query = query.filter(Funcionario.departamento.ilike(f'%{setor}%'))  

    funcionarios_encontrados = query.all()  
    return render_template('resultado.html', funcionarios=funcionarios_encontrados)

if __name__ == '__main__':
    app.run(debug=True)
