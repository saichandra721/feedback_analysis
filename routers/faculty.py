from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import database, models

router = APIRouter(
    prefix='/faculty',
    tags = ['Faculty']
)

get_db = database.get_db

"""
This api returns all faculty and their subjects
"""
@router.get('/')
def getFaculty(db: Session = Depends(get_db)):

    return "returning all faculties"

"""
return feedback of the subject
"""
@router.get('/feedback')
def getFeedback(db: Session = Depends(get_db)):
    pass

"""
return all feedbacks for a particular faculty
"""
@router.get('/all_feedbacks')
def getAllFeedbacksForFaculty(db: Session = Depends(get_db)):
    pass