# Sistema de Agendamento para Barbearia

Sistema web de agendamento de horários, desenvolvido do zero como projeto de aprendizado.

## Funcionalidades

- Cadastro e listagem de serviços (via API)
- Cadastro de usuários via API (clientes e prestadores)
- Configuração de horários de expediente por dia da semana
- Algoritmo de disponibilidade (considera a duração do serviço e os agendamentos existentes)
- Interface web para o cliente escolher serviço, data e horário disponível
- Agendamento com atualização automática da interface após a confirmação

## Tecnologias

- **Backend:** Python, Flask, SQLAlchemy
- **Banco de dados:** SQLite
- **Frontend:** HTML, CSS, JavaScript (vanilla)

## Como rodar localmente

1. Clone o repositório e entre na pasta:

```
git clone https://github.com/PereiraRichard/agendamento-barbearia.git
cd agendamento-barbearia
```

2. Crie e ative o ambiente virtual (Windows):

```
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Rode o servidor:

```
python app.py
```

5. Acesse `http://127.0.0.1:5000` no navegador.

O banco começa vazio. Cadastre serviços, um prestador e os horários de expediente pela API (rotas `/servicos`, `/usuarios` e `/horarioDisponivel`, via POST).

## Próximos passos

- Tela de cadastro/login de cliente
- Painel de administração para o prestador
- Layout responsivo para celular
- Senhas com hash e tratamento de dias sem expediente
