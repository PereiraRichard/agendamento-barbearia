from models import db, Servico, Usuario, HorarioDisponivel, Agendamento
from flask import Flask, jsonify, request, render_template
from datetime import datetime, timedelta, date
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/servicos')
def listar_servicos():
    servicos = Servico.query.all()
    resultado = []
    for s in servicos:
        resultado.append({'id': s.id, 'nome': s.nome, 'duracao': s.duracao, 'preco': s.preco})
    return jsonify(resultado)

@app.route('/servicos', methods=['POST'])
def criar_servico():
    dados = request.get_json()
    novo_servico = Servico(nome=dados['nome'], duracao=dados['duracao'], preco=dados['preco'])
    db.session.add(novo_servico)
    db.session.commit()
    return jsonify({'mensagem': 'Serviço criado com sucesso!'})

@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    resultado = []
    for s in usuarios:
        resultado.append({'id': s.id, 'nome': s.nome, 'email': s.email, 'tipo': s.tipo})
    return jsonify(resultado)

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    novo_usuario = Usuario(
        nome=dados['nome'],
        email=dados['email'],
        tipo=dados['tipo'],
        senha=generate_password_hash(dados['senha'])
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuario criado com sucesso'})

@app.route('/horarioDisponivel')
def listar_horarios():
    horarios = HorarioDisponivel.query.all()
    resultado = []
    for s in horarios:
        resultado.append({
            'id': s.id,
            'prestador_id': s.prestador_id,
            'dia_semana': s.dia_semana,
            'hora_inicio': s.hora_inicio.strftime('%H:%M:%S'),
            'hora_fim': s.hora_fim.strftime('%H:%M:%S')
        })
    return jsonify(resultado)

@app.route('/horarioDisponivel', methods=['POST'])
def criar_horario():
    dados = request.get_json()
    hora_inicio = datetime.strptime(dados['hora_inicio'], '%H:%M:%S').time()
    hora_fim = datetime.strptime(dados['hora_fim'], '%H:%M:%S').time()
    novo_horario = HorarioDisponivel(prestador_id=dados['prestador_id'], dia_semana=dados['dia_semana'], hora_inicio=hora_inicio, hora_fim=hora_fim)
    db.session.add(novo_horario)
    db.session.commit()
    return jsonify({'mensagem': 'Horario criado com sucesso!'})

@app.route('/agendamentos')
def listar_agendamentos():
    agendamentos = Agendamento.query.all()
    resultado = []
    for a in agendamentos:
        resultado.append({
            'id': a.id,
            'cliente_id': a.cliente_id,
            'servico_id': a.servico_id,
            'data': a.data.strftime('%Y-%m-%d'),
            'horas': a.horas.strftime('%H:%M:%S'),
            'status': a.status
        })
    return jsonify(resultado)

@app.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    dados = request.get_json()
    data = datetime.strptime(dados['data'], '%Y-%m-%d').date()
    horas = datetime.strptime(dados['horas'], '%H:%M:%S').time()
    novo_agendamento = Agendamento(
        cliente_id=dados['cliente_id'],
        servico_id=dados['servico_id'],
        data=data,
        horas=horas
    )
    db.session.add(novo_agendamento)
    db.session.commit()
    return jsonify({'mensagem': 'Agendamento criado com sucesso!'})


@app.route('/disponibilidade')
def verificar_disponibilidade():
    prestador_id = request.args.get('prestador_id')
    dia_semana = request.args.get('dia_semana')
    servico_id = request.args.get('servico_id')
    data_str = request.args.get('data')

    expediente = HorarioDisponivel.query.filter_by(prestador_id=prestador_id, dia_semana=dia_semana).first()
    servico = Servico.query.get(servico_id)

    if expediente is None or servico is None:
        return jsonify([])

    duracao = timedelta(minutes=servico.duracao)

    horario_atual = datetime.combine(datetime.today(), expediente.hora_inicio)
    horario_fim = datetime.combine(datetime.today(), expediente.hora_fim)

    slots = []
    while horario_atual + duracao <= horario_fim:
        slots.append(horario_atual.strftime('%H:%M:%S'))
        horario_atual = horario_atual + duracao

    data_pesquisada = datetime.strptime(data_str, '%Y-%m-%d').date()
    agendamentos_do_dia = Agendamento.query.filter_by(data=data_pesquisada, status='confirmado').all()
    horarios_ocupados = [a.horas.strftime('%H:%M:%S') for a in agendamentos_do_dia]

    slots_disponiveis = [s for s in slots if s not in horarios_ocupados]

    return jsonify(slots_disponiveis)

if __name__ == '__main__':
    app.run(debug=True)
