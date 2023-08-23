from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Category, Entry, Tag

if __name__ == "__main__":
    engine = create_engine("sqlite:///password_manager.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb

    ipdb.set_trace()
