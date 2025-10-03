from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


#os is giving python the terminal and letting it do what users can do with terminal 
#.getenv means to access environment variable 
#.getenv(x,y) if x is not found, fall back to y 
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database/todos.db")

#connector between Python and the database 
engine = create_engine(DATABASE_URL)

#sessionmaker is a factory of sessions
#a session is basically giving Python ORM features 
#ORM = Object-related mapping 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

