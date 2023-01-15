from typing import Optional, List, Dict

from pydantic import BaseModel


class ResponseModel(BaseModel):
    class Config():
        orm_mode = True


class UserModel(BaseModel):
    name: str
    password: str
    account: str


class FacultyModel(BaseModel):
    name: str
    subject: str
    score: str
    feed: Optional[Dict] = None


class GetFacultyResponseModel(BaseModel):
    allFaculty: List[FacultyModel] = []


class GetFeedbackRequestModel(BaseModel):
    name: str
    subject: str
class GetFeedbackResponseModel(BaseModel):
    name: str
    subject: str
    score: str
    feed: Optional[Dict] = None


class GetAllFeedbacksForFacultyResponseModel(FacultyModel):
    removeThis: bool = True


class StudentModel(BaseModel):
    name: str
    feed: Optional[Dict] = None


class GetAllStudentsResponseModel(BaseModel):
    students: Optional[List[StudentModel]] = None


class GetFeedbackFromStudentResponseModel(StudentModel):
    pass


class SendFeedback(BaseModel):
    pass