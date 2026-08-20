# Sistema de Agendamento para Barbearia

Sistema web completo de agendamento de horários, desenvolvido do zero como projeto de aprendizado.

## Funcionalidades

- Cadastro e listagem de serviços (via API)
- Cadastro de usuários via API (clientes e prestadores)
- Configuração de horários de expediente por dia da semana
- Algoritmo de verificação de disponibilidade (considera duração do serviço e agendamentos existentes)
- Interface web para o cliente escolher serviço, data e horário disponível
- Agendamento de horários com atualização automática da interface após confirmação

## Tecnologias utilizadas

- **Backend:** Python, Flask, SQLAlchemy
- **Banco de dados:** SQLite
- **Frontend:** HTML, CSS, JavaScript (vanilla)

## Como rodar o projeto localmente

1. Clone o repositório
2. Instale as dependências:
3. Rode o servidor:
4. Acesse `http://127.0.0.1:5000` no navegador

## Próximos passos

- Tela de cadastro/login de cliente na interface
- Página de administração para o prestador gerenciar agendamentos
- Estilização responsiva para dispositivos móveis

## Sobre o projeto

Este projeto foi desenvolvido para praticar conceitos de desenvolvimento web full stack: modelagem de banco de dados relacional, criação de API REST, lógica de negócio (algoritmo de disponibilidade), e integração entre frontend e backend.
