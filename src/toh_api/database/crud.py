from typing import List
from sqlalchemy.orm import Session

from . import models, schemas



def get_hero(db: Session, hero_id: int):
    return db.query(models.Heroes).filter(models.Heroes.id == hero_id).first()


def get_heroes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Heroes).offset(skip).limit(limit).all()


def search_heroes(db: Session, name: str, skip: int = 0, limit: int = 100):
    search_result = []
    for hero in get_heroes(db, skip, limit):
        if name in hero.name.lower():
            search_result.append(hero)
    return search_result


def create_hero(db: Session, hero: schemas.HeroCreate):
    db_hero = models.Heroes(name = hero.name)
    db.add(db_hero)
    db.commit()
    db.refresh(db_hero)
    return db_hero


def update_hero(db: Session, hero_id: int, hero_name: str):
    db_hero = db.query(models.Heroes).filter(models.Heroes.id == hero_id).first()
    db_hero.name = hero_name
    db.commit()
    db.refresh(db_hero)
    return db_hero


def delete_hero(db: Session, hero_id: int):
    db.query(models.Heroes).filter(models.Heroes.id == hero_id).delete()
    db.commit()