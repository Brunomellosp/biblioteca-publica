
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
import database

class Usuario(database.Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    telefone = Column(String(50), nullable=True)
    endereco = Column(String(255), nullable=True)

    # caminhos relativos para os arquivos enviados
    documento_path = Column(String(255), nullable=True)
    comprovante_path = Column(String(255), nullable=True)

    status = Column(String(50), nullable=False, default="ativo")
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
