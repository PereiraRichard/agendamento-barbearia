from werkzeug.security import generate_password_hash
from app import app
from models import db, Servico, Usuario, HorarioDisponivel
from datetime import time

with app.app_context():
    if Usuario.query.count() == 0:
        db.session.add(Usuario(
            nome='Carlos Barbeiro',
            email='carlos@exemplo.com',
            senha=generate_password_hash('123456'),
            tipo='prestador'
        ))
        db.session.add_all([
            Servico(nome='Corte de cabelo', duracao=30, preco=40.0),
            Servico(nome='Barba', duracao=30, preco=30.0),
            Servico(nome='Corte + Barba', duracao=60, preco=65.0),
        ])
        for dia in ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']:
            db.session.add(HorarioDisponivel(
                prestador_id=1,
                dia_semana=dia,
                hora_inicio=time(9, 0),
                hora_fim=time(18, 0)
            ))
        db.session.commit()
        print('Dados de exemplo criados!')
    else:
        print('O banco já tem dados.')
