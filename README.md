# Academia Churn API

API REST desenvolvida em Python com FastAPI para
gerenciar alunos de academia, registrar presenças
e identificar possíveis riscos de desistência.

## Objetivo

Demonstrar a aplicação de Python, APIs REST,
bancos de dados relacionais e regras de negócio
em um cenário de retenção de clientes.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest

## Funcionalidades

- Cadastro de alunos
- Registro de check-ins
- Consulta de frequência nos últimos 7 dias
- Classificação básica de risco de churn
- Validação de dados
- Tratamento de erros HTTP

## Regra de risco

- Menos de 3 check-ins nos últimos 7 dias:
  risco atribuído de 80%.
- 3 ou mais check-ins:
  risco atribuído de 20%.

Os percentuais são regras demonstrativas.
Não representam probabilidades calculadas
por um modelo de Machine Learning.

## Instalação

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
uvicorn app.main:app --reload
```

Acesse a documentação interativa:

http://127.0.0.1:8000/docs

## Testes

```bash
python -m pytest tests/ -v
```

## Próximas melhorias

- Cadastro de planos pela API
- Prevenção de check-ins duplicados
- Testes isolados com banco temporário
- Modelo preditivo de Machine Learning
- Dashboard de acompanhamento
