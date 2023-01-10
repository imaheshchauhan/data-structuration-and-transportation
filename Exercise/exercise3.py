import csv

class Student:
    def __init__(self, id, name, city, school) -> None:
       self.id = id
       self.name = name
       self.city = city
       self.school = school

    def __repr__(self) -> str:
        return f'Id: {self.id}, Name: {self.name}, City: {self.city}, School: {self.school}'


def csvReader() -> list :
    data = [] 
    with open("resources/csv/users.csv", 'r') as file:
        csvreader = csv.reader(file)
        csvreader.__next__()
        for lines in csvreader:

            data.append(Student(lines[0],lines[1],lines[2],lines[3]))

    return data            

print(csvReader())
