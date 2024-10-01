from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost/funcionarios"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo da tabela funcionarios
class Funcionario(db.Model):
    __tablename__ = 'funcionarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Numeric(10, 2), nullable=False)
    departamento = db.Column(db.String(50), nullable=False)
    loja = db.Column(db.String(50), nullable=False)
    data_contratacao = db.Column(db.Date, nullable=False)
    data_demissao = db.Column(db.Date, nullable=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    nome = request.form.get('nome', '').strip()  # Obtenha e limpe o campo 'nome'
    setor = request.form.get('setor', '').strip()  # Obtenha e limpe o campo 'setor'
    
    # Se ambos os campos estiverem vazios, retorne uma mensagem ou uma página vazia
    if not nome and not setor:
        return render_template('resultado.html', funcionarios=[], mensagem="Por favor, insira um nome ou setor para a busca.")
    
    # Inicialize a query básica sem filtros
    query = Funcionario.query
    
    # Adiciona filtro se o nome foi fornecido
    if nome:
        query = query.filter(Funcionario.nome.ilike(f'%{nome}%'))
    
    # Adiciona filtro se o setor foi fornecido
    if setor:
        query = query.filter(Funcionario.departamento.ilike(f'%{setor}%'))
    
    # Execute a consulta com os filtros adicionados, se houver
    funcionarios_encontrados = query.all()

    return render_template('resultado.html', funcionarios=funcionarios_encontrados)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cargo = request.form.get('cargo')
        salario = request.form.get('salario')
        departamento = request.form.get('departamento')
        loja = request.form.get('loja')
        data_contratacao = request.form.get('data_contratacao')

        novo_funcionario = Funcionario(
            nome=nome,
            cargo=cargo,
            salario=salario,
            departamento=departamento,
            loja=loja,
            data_contratacao=data_contratacao
        )
        
        db.session.add(novo_funcionario)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('adicionar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    funcionario = Funcionario.query.get_or_404(id)

    if request.method == 'POST':
        funcionario.nome = request.form.get('nome')
        funcionario.cargo = request.form.get('cargo')
        funcionario.salario = request.form.get('salario')
        funcionario.departamento = request.form.get('departamento')
        funcionario.loja = request.form.get('loja')
        funcionario.data_demissao = request.form.get('data_demissao')

        db.session.commit()
        return redirect(url_for('resultado'))

    return render_template('editar.html', funcionario=funcionario)


@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    funcionario = Funcionario.query.get(id)
    
    if not funcionario:
        return "Funcionário não encontrado", 404

    funcionario.nome = request.form['nome']
    funcionario.cargo = request.form['cargo']
    funcionario.salario = request.form['salario']
    funcionario.departamento = request.form['departamento']
    funcionario.loja = request.form['loja']
    funcionario.data_contratacao = request.form['data_contratacao']
    demitido = request.form.get('demitido')
    
    if demitido:
        funcionario.demitido = True
        funcionario.data_demissao = request.form['data_demissao'] if request.form.get('data_demissao') else None
    else:
        funcionario.demitido = False
        funcionario.data_demissao = None

    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
