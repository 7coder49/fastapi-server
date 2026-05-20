from app.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    dept = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(100))
