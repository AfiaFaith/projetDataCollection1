from cgitb import text
from numpy import double
from sqlalchemy import Boolean, Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Devise(Base):
    __tablenames__ = "tb_projet"

    id = Column(Integer, primary_key=True, index=True)
    Devise = Column(text)
    Achat = Column(double)
    Vente = Column(double)
    new_devise = Column(double)
    XOF_conversion  = Column(double)
    Pays = Column(text)
    Flag = Column(text)

    

    items = relationship("dbpro", back_populates="owner")


