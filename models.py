from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer)
    plano_id = Column(Integer, ForeignKey("planos.id"))
    plano = relationship("Plano")

class Checkin(Base):
    __tablename__ = 'checkins'
    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    data_checkin = Column(String)

class Plano(Base):
    __tablename__ = 'planos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Integer)
