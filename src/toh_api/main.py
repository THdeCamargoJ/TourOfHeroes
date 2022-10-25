from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.db import get_engine_from_settings, get_session


import json



engine = get_engine_from_settings()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


def get_database():
    db = get_session(engine)
    try:
        yield db
    finally:
        db.close()


@app.post('/heroes/', response_model=schemas.Hero)
def create_hero(hero: schemas.HeroCreate, database: Session = Depends(get_database)):
    return crud.create_hero(db=database, hero=hero)


@app.get('/heroes/', response_model=List[schemas.Hero])
def read_heroes(skip: int = 0, limit: int = 100, database: Session = Depends(get_database)):
    return crud.get_heroes(db=database, skip=skip, limit=limit)


@app.get('/heroes/?name={hero_name}', response_model=List[schemas.Hero])
def search_heroes(hero_name: str, skip: int = 0, limit: int = 100, database: Session = Depends(get_database)):
    return crud.search_heroes(db=database, name=hero_name, skip=skip, limit=limit)


@app.get('/heroes/{hero_id}', response_model=schemas.Hero)
def read_hero(hero_id: int, database: Session = Depends(get_database)):
    hero = crud.get_hero(db=database, hero_id=hero_id)
    if hero is None:
        raise HTTPException(status_code=404, detail='Hero not found')
    return hero


@app.put('/heroes/')
async def update_hero(request: Request, database: Session = Depends(get_database)):
    hero = await request.json()
    return crud.update_hero(db=database, hero_id=hero['id'], hero_name=hero['name'])


@app.delete('/heroes/{hero_id}')
def delete_hero(hero_id: int, database: Session = Depends(get_database)):
    crud.delete_hero(db=database, hero_id=hero_id)