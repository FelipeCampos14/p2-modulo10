from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
metadata_obj = MetaData()

# Database Configuration
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@database:5432/prova2"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

metadata_obj.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)