
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, crud, schemas, database

app = FastAPI(title="Academia Churn API")

database.Base.metadata.create_all(bind=database.engine)

@app.post("/aluno/registro")
def registro_aluno(
    aluno: schemas.AlunoCreate,
    db: Session = Depends(database.get_db)
):
    plano = db.query(models.Plano).filter(
        models.Plano.id == aluno.plano_id
    ).first()

    if plano is None:
        raise HTTPException(
            status_code=404,
            detail="Plano não encontrado"
        )

    return crud.registrar_aluno(aluno, db)

@app.post("/aluno/checkin")
def checkin_aluno(
    checkin: schemas.CheckinCreate,
    db: Session = Depends(database.get_db)
):

    aluno = db.query(models.Aluno).filter(
        models.Aluno.id == checkin.aluno_id
    ).first()

    if aluno is None:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return crud.registrar_checkin(checkin, db)


@app.get("/aluno/{id}/frequencia")
def frequencia_aluno(
    id: int,
    db: Session = Depends(database.get_db)
):
    aluno = db.query(models.Aluno).filter(
        models.Aluno.id == id
    ).first()

    if aluno is None:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return crud.obter_frequencia(id, db)

@app.get("/aluno/{id}/risco-churn")
def risco_churn(
    id: int,
    db: Session = Depends(database.get_db)
):
    aluno = db.query(models.Aluno).filter(
        models.Aluno.id == id
    ).first()

    if aluno is None:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return crud.calcular_risco_churn(id, db)
