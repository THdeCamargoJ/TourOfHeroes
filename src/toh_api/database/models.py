from sqlalchemy import Column, Integer, String

from database.db import get_Base



Base = get_Base()



class Heroes(Base):
    __tablename__ = 'hero'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)