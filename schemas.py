
from datetime import date
from pydantic import BaseModel, Field

class AlunoCreate(BaseModel):
    nome: str = Field(min_length=2)
    idade: int = Field(ge=1, le=120)
    plano_id: int = Field(gt=0)

class CheckinCreate(BaseModel):
    aluno_id: int = Field(gt=0)
    data_checkin: date

class Frequencia(BaseModel):
    aluno_id: int
    frequencia_semana: int

class RiscoChurn(BaseModel):
    aluno_id: int
    probabilidade_churn: float
