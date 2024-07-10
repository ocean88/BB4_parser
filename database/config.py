from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Настройка подключения к базе данных SQLite
DATABASE_URL = "sqlite:///skypro_diplom.db"
print("DATABASE_URL:", DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()