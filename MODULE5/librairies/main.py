from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import dbstructure, apistruct
from .database import engine, SessionLocal

dbstructure.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tb_projet/", response_model=list[schemas.tb_projet])
def read_tb_projet(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tb_projet = crud.get_tb_projet(db, skip=skip, limit=limit)
    return tb_projet

