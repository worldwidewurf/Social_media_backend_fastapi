from fastapi import FastAPI,Response,status,Depends,HTTPException,APIRouter
from sqlalchemy.orm import Session
from .. import schemas,database,aouth2,models
router = APIRouter(
    prefix="/vote",
    tags=["vote"]
    )
@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote,db: Session = Depends(database.get_db),current_user: int = Depends(aouth2.get_current_user)):
    """_summary_ : This function creates a new vote.

    Args:
        vote (schemas.Vote): vote to be created.
        db (Session, optional): _description_. Defaults to Depends(database.get_db).
        current_user (int, optional): _description_. Defaults to Depends(aouth2.get_current_user).

    Raises:
        HTTPException: _description_
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        _type_: Dict[str, str]
    """
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {vote.post_id} not found"
        )

    vote_query = (db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,models.Vote.user_id == current_user.id))
    found_vote = vote_query.first()
    
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {current_user.id} has already voted on post {vote.post_id}"
            )
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Successfully voted!"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vote does not exist"
            )
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Successfully deleted vote"}