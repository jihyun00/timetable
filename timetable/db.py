from alembic.config import Config
from annotation.typed import optional, typechecked
from flask import Flask, current_app, g
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as SqlalchemySession, sessionmaker
from werkzeug.local import LocalProxy


__all__ = ('Base', 'ensure_shutdown_session', 'get_engine', 'get_session',
           'session', 'Session')


@typechecked
def ensure_shutdown_session(app: Flask):
    def close_session(exc=None):
        if hasattr(g, 'sess'):
            if exc:
                g.sess.rollback()
            g.sess.close()

    app.teardown_appcontext(close_session)


@typechecked
def get_engine(config: dict=None) -> Engine:
    if config is None:
        config = current_app.config
    if 'DATABASE_ENGINE' in config:
        return config['DATABASE_ENGINE']
    config['DATABASE_ENGINE'] = create_engine(config['DATABASE_URL'])
    return config['DATABASE_ENGINE']


@typechecked
def get_alembic_config(engine: Engine) -> Config:
    if not isinstance(engine, Engine):
        raise Exception('boilerplate.db.get_alembic_config: engine is not'
                        '`Engine`')
    config = Config()
    config.set_main_option('script_location', 'soran:migrations')
    config.set_main_option('sqlalchemy.url', str(engine.url))
    return config


@typechecked
def get_session(engine: optional(Engine)=None) -> SqlalchemySession:
    if engine is None:
        engine = get_engine()
    if hasattr(g, 'sess'):
        return g.sess
    session = Session(bind=engine)
    try:
        g.sess = session
    except RuntimeError:
        pass
    return session


Base = declarative_base()
Session = sessionmaker()
session = LocalProxy(get_session)
