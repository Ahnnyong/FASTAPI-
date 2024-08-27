# models.py

from sqlalchemy import Column, Integer, String
from database import Base

class Post(Base):
    __tablename__ = "posts"  # 이 줄을 추가하여 테이블 이름을 지정합니다

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
