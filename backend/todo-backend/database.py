from sqlmodel import create_engine, Session, SQLModel
from models import *
import os

# Get database URL from environment (fallback to sqlite if not set)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo.db")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session