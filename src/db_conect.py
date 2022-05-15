from sqlalchemy import create_engine, MetaData
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as _declarative


DB_URL = "sqlite:///./data.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

session_db = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = _declarative.declarative_base()

def create_db():
    return base.metadata.create_all(bind=engine)
