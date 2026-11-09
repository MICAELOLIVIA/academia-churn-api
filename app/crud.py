from sqlalchemy.orm import Session
from app import models, schemas

def registrar_aluno(aluno: schemas.AlunoCreate, db: Session):
    db_aluno = models.Aluno(nome=aluno.nome, idade=aluno.idade, plano_id=aluno.plano_id)
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

def registrar_checkin(checkin: schemas.CheckinCreate, db: Session):
    db_checkin = models.Checkin(aluno_id=checkin.aluno_id, data_checkin=checkin.data_checkin.isoformat())
    db.add(db_checkin)
    db.commit()
    db.refresh(db_checkin)
    return db_checkin


def obter_frequencia(id: int, db: Session):
    from datetime import date, timedelta

    hoje = date.today()
    inicio_periodo = hoje - timedelta(days=6)

    return db.query(models.Checkin).filter(
        models.Checkin.aluno_id == id,
        models.Checkin.data_checkin >= inicio_periodo.isoformat(),
        models.Checkin.data_checkin <= hoje.isoformat()
    ).count()


def calcular_risco_churn(id: int, db: Session):
    frequencia = obter_frequencia(id, db)

    if frequencia < 3:
        return schemas.RiscoChurn(
            aluno_id=id,
            probabilidade_churn=0.8
        )

    return schemas.RiscoChurn(
        aluno_id=id,
        probabilidade_churn=0.2
    )
