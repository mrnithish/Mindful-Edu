from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

students={
    1:{
        "name": "tom",
        "age": 15,
        "year":"year 12"
    }
}
class Student(BaseModel):
    name:str
    age:int
    year:str
    
class UpdateStudent(BaseModel):
    name: Optional[str]=None
    age:  Optional[int]=None
    year: Optional[str]=None

#head
@app.get("/")
def index():
    return "Home"

#get method
@app.get("/get-student/{student_id}")
def get_student(student_id : int):
    return students[student_id]

#get Query Parameter
@app.get("/get-by-name")
def get_student(name:str):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not Found"}


#post
@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return "Student Exit"
    
    students[student_id]=student
    return students[student_id]

#put
@app.put("/update-student/{student_id}")
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in students:
        return {"Data":"Not Exist"}
    
    # if student.name!=None:
    #     students[student_id].name=student.name

    # if student.age!=None:
    #     students[student_id].age=student.age

    # if student.year!=None:
    #     students[student_id].year=student.year
    students[student_id]=student
    return students[student_id]

#delete
@app.delete("/delete_student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Data":"Not Exist"}
    del students[student_id]
    return {"Message":"Record deleted"}

    


