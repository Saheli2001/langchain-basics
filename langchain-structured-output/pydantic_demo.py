from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'nitish'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=2, description="CGPA should be between 0 and 10")

# new_student = {'name': 32} #error throws
# new_student = {'age': '32'} #type coarsing
new_student = {'email': 'saheli@example.com', 'cgpa': 8.5} #valid
student = Student(**new_student)

print(student)
print(dict(student))
print(student.model_dump_json())