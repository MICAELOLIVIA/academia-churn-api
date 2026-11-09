
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_aluno_inexistente():
    resposta = client.get(
        "/aluno/999999/risco-churn"
    )
    assert resposta.status_code == 404

def test_checkin_aluno_inexistente():
    resposta = client.post(
        "/aluno/checkin",
        json={
            "aluno_id": 999999,
            "data_checkin": "2026-11-09"
        }
    )
    assert resposta.status_code == 404

def test_idade_invalida():
    resposta = client.post(
        "/aluno/registro",
        json={
            "nome": "João",
            "idade": -5,
            "plano_id": 1
        }
    )
    assert resposta.status_code == 422
