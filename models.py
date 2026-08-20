from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(20), nullable=False, default='cliente')

class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    duracao = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)

class HorarioDisponivel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prestador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)   
    dia_semana = db.Column(db.String(20), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fim = db.Column(db.Time, nullable=False)

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey('servico.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    horas = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='confirmado')
     