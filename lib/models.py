from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///password_manager.db")

Base = declarative_base()