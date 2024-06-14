import logging
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from database.database import SessionLocal, Base, engine
from database.models import BlogPostDB
from database.schemas import BlogCreate, BlogPost
from logging_config import LoggerSetup
import logging

# Cria um logger raiz
logger_setup = LoggerSetup()

# Adiciona o logger para o módulo
LOGGER = logging.getLogger(__name__)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post('/blog', response_model=BlogPost)
async def create_blog_post(blog_post: BlogCreate, db: Session = Depends(get_db)):
    try:
        post = BlogPostDB(title=blog_post.title, content=blog_post.content)
        db.add(post)
        db.commit()
        db.refresh(post)
        db.close()
        LOGGER.info(f" Blog Post com id {post.id} foi criado.")
        return post
    except KeyError:
        LOGGER.error(f"Blog Post com id {post.id} não foi encontrado.")
        return HTTPException(status_code=400, detail="Invalid request") 
    except Exception as e:
        LOGGER.error(f"Blog Post com id {post.id} não foi encontrado.")
        raise HTTPException(status_code=500, detail=f"error: {str(e)}") 


@app.get("/blog", response_model=List[BlogPost])
async def get_blog_posts(db: Session = Depends(get_db)):
    LOGGER.info({"message": "Acessando a rota /blog", "method": "GET"})
    blog_posts = db.query(BlogPostDB).all()
    db.close()
    if blog_posts == []:
        LOGGER.warning(f" Blog Post ainda não foram cirado.")
    return blog_posts


@app.get("/blog/{post_id}", response_model=BlogPost)
def get_blog_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(BlogPostDB).filter(BlogPostDB.id == post_id).first()
    db.close()
    if post is None:
        LOGGER.warning(f" Blog Post com id {post_id} não foi encontrado.")
        raise HTTPException(status_code=404, detail="Blog post not found")
    LOGGER.info(f" Blog Post com id {post_id} foi encontrado.")
    return post


@app.put("/blog/{post_id}", response_model=BlogPost)
async def update_todo(post_id: int, post:BlogCreate, db: Session = Depends(get_db)):
    post_db = db.query(BlogPostDB).filter(BlogPostDB.id == post_id).first()
    if post_db is None:
        db.close()
        LOGGER.warning(f"Blog Post com id {post_id} não foi encontrado.")
        raise HTTPException(status_code=404, detail="Blog Post not found")
    if post_db.title is not None:
        post_db.title = post.title
    if post_db.content is not None:
        post_db.content = post.content
    db.commit()
    db.refresh(post_db)
    db.close()
    return post_db


@app.delete("/blog/{post_id}", response_model=BlogPost)
async def delete_blog_post(post_id: int, db: Session = Depends(get_db)):
    try:
        post = db.query(BlogPostDB).filter(BlogPostDB.id == post_id).first()
        db.delete(post)
        db.commit()
        db.close()
        if post is None:
            LOGGER.warning(f" Blog Post com id {post_id} não foi encontrado.")
            raise HTTPException(status_code=404, detail="User not found")
        LOGGER.info(f" Blog Poost com id {post_id} foi removido.")
        return post
    except KeyError:
        LOGGER.error(f"Blog Post com id {post_id} não foi encontrado.")
        return HTTPException(status_code=400, detail="Invalid request") 
    except Exception as e:
        LOGGER.error(f"Blog Post com id {post_id} não foi encontrado.")
        raise HTTPException(status_code=500, detail=f"error: {str(e)}") 
