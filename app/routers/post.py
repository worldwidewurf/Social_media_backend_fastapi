from typing import List, Optional
from .. import models,schemas,aouth2
from fastapi import  FastAPI, HTTPException, Response, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from sqlalchemy import func

router = APIRouter(
    prefix= "/posts",
    tags= ["Posts"],
)
@router.get("/",response_model=List[schemas.PoesOut])
def get_posts(db: Session = Depends(get_db) ,current_user: int = Depends(aouth2.get_current_user),limit:int = 10,skip:int = 0,search:Optional[str] = ""):
    # posts = db.query(models.Post).filter(models.Post.title.ilike("%"+search+"%")).limit(limit).offset(skip).all()
    """_summary_ : This function returns a list of posts.

    Args:
        db (Session, optional): database session. Defaults to Depends(get_db).
        current_user (int, optional): _description_. Defaults to Depends(aouth2.get_current_user).
        limit (int, optional): _description_. Defaults to 10.
        skip (int, optional): _description_. Defaults to 0.
        search (Optional[str], optional): _description_. Defaults to "".

    Returns:
        _type_: List[schemas.PoesOut]
    """
    results = db.query(models.Post,func.count(models.Vote.post_id).label('votes')).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.ilike("%"+search+"%")).limit(limit).offset(skip).all()
    
    return results


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(aouth2.get_current_user)):
    """_summary_ : This function creates a new post.

    Args:
        post (schemas.PostCreate): post to be created.
        db (Session, optional): database session. Defaults to Depends(get_db).
        current_user (int, optional): the user creating the post as verified by the token id. Defaults to Depends(aouth2.get_current_user).

    Returns:
        _type_: schemas.PostResponse
    """
    created_post = models.Post(owner_id =current_user.id, **post.dict())
    db.add(created_post) 
    db.commit()
    db.refresh(created_post)
    return created_post


@router.get("/{post_id}", response_model=schemas.PoesOut)
def get_post(post_id: int, db: Session = Depends(get_db),current_user: int = Depends(aouth2.get_current_user)):
    # post = db.query(models.Post).filter(models.Post.id == post_id).first()
    """_summary_ : This function returns a single post.

    Args:
        post_id (int): id of the post to be returned.
        db (Session, optional): _description_. Defaults to Depends(get_db).
        current_user (int, optional): _description_. Defaults to Depends(aouth2.get_current_user).

    Raises:
        HTTPException: raised when the post with the given id is not found

    Returns:
        _type_: schemas.PoesOut
    """
    post = db.query(models.Post,func.count(models.Vote.post_id).label('votes')).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")
    
    return post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db),current_user: int = Depends(aouth2.get_current_user)):
    """_summary_ : This function deletes a post.

    Args:
        post_id (int): id of the post to be deleted.
        db (Session, optional): _description_. Defaults to Depends(get_db).
        current_user (int, optional): _description_. Defaults to Depends(aouth2.get_current_user).

    Raises:
        HTTPException: raised when the post with the given id is not found
        HTTPException: raised when the post is not owned by the person trying to delete it

    Returns:
        _type_: Response
    """
    deleted_post = db.query(models.Post).filter(models.Post.id == post_id)
    if deleted_post.first() == None:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")
    if deleted_post.first().owner_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"Post with id {post_id} not owned by user {current_user.id}")
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{post_id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.PostResponse)
def update_post(post_id: int, post: schemas.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(aouth2.get_current_user) ):
    """_summary_ : This function updates a post.

    Args:
        post_id (int): id of the post to be updated.
        post (schemas.PostCreate): the updated post.
        db (Session, optional): _description_. Defaults to Depends(get_db).
        current_user (int, optional): _description_. Defaults to Depends(aouth2.get_current_user).

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        _type_: schemas.PostResponse
    """
    updated_post = db.query(models.Post).filter(models.Post.id == post_id)
    uppost = updated_post.first()
    if not uppost:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} not found")
    if uppost.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail=f"Post with id {post_id} not owned by user {current_user.id}")
    updated_post.update(post.dict(),synchronize_session=False)
    db.commit()
    return updated_post.first()
