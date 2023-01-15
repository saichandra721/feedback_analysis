from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import database, models

router = APIRouter(
    prefix='/student',
    tags = ['Student']
)

get_db = database.get_db

"""
return all students
"""
@router.get('/')
def getStudents(db: Session = Depends(get_db)):
    students = db.query(models.User).filter(models.User.account=='student').all()
    return students

"""
get all feedbacks of a particular student
"""
@router.get('/feedback')
def getFeedbackFromStudent(db: Session = Depends(get_db)):

    pass


"""
send feedback to a faculty
"""
@router.post('/feedback')
def sendFeedback(request, db: Session = Depends(get_db)):
    pass