from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, create_database

from database.db_config import settings



def get_engine(db_type, user, password, host, port, db_name):
    url = f'{db_type}://{user}:{password}@{host}:{port}/{db_name}'
    
    if not database_exists(url):
        create_database(url)
    
    return create_engine(url)


def get_engine_from_settings():
    keys = ['db_type', 'user', 'pass', 'host', 'port', 'db_name']
    
    if not all(key in keys for key in settings.keys()):
        raise Exception(
            "The settings file must contain all 'db_type', 'user', 'password', \
                'host', 'port' and 'db_name' keys."
        )

    return get_engine(
        settings['db_type'],
        settings['user'],
        settings['pass'],
        settings['host'],
        settings['port'],
        settings['db_name']
    )


def get_session(engine=None):
    if engine is None:
        engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session


def get_Base():
    engine = get_engine_from_settings()
    Base = declarative_base(engine)
    return Base