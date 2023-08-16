from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Category, Entry, engine

Session = sessionmaker(bind=engine)
session = Session()

session.query(Entry).delete()
session.query(Category).delete()
session.query(User).delete()
session.commit()
