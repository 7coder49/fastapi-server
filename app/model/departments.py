from sqlalchemy import Column, Integer, String

from app.database import Base


class Department(Base):
    __tablename__ = "departments"
    id=Column(Integer, primary_key=True)
    name=Column(String(100), nullable=False)
    subject=Column(String(100), nullable=False)