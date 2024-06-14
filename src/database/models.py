from sqlalchemy import Column, Integer, String
from .database import Base

class BlogPostDB(Base):
  __tablename__ = 'blog_post'

  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(50), nullable=False)
  content = Column(String(255), nullable=False)

  def __repr__(self):
    return f'<User:[id:{self.id}, title:{self.title}, content:{self.content}]>'
    
  def serialize(self):
    return {
      "id": self.id,
      "title": self.title,
      "content": self.content
    }