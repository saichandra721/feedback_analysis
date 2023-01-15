from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import database
import models
import schemas

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db

@router.post('/login')
def login(request: schemas.UserModel, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, password=request.password, account=request.account)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.__dict__
# def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
#     pass
    # user = db.query(models.User).filter(models.User.email == request.username).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Invalid Credentials")
    # if not Hash.verify(user.password, request.password):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Incorrect password")
    #
    # access_token = token.create_access_token(data={"sub": user.email})
    # return {"access_token": access_token, "token_type": "bearer"}