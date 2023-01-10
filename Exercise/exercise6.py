import json
  
class Student:
    id: int
    name: str
    city: str
    school: str
    age: int
    isTeacher: bool

    def __repr__(self) -> str:
        return f'{self.id}  {self.name} {self.city} {self.school}   {self.age}  {self.isTeacher}'

studentList = []
with open("resources/json/users.json", 'r') as file:
    jsonData = json.load(file)
    for student in jsonData:
        std = Student()
        std.id = student['id']
        std.name = student['name']
        std.city = student['city']
        std.school = student['school']
        std.age = student['age']
        std.isTeacher = student['is_teacher']
        studentList.append(std)
print(studentList)

