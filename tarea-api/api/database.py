from sqlmodel import Session, SQLModel, create_engine

from api.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

connect_args={'check_same_thread':False}

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session