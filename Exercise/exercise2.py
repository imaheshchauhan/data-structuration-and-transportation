class User:
    def __init__(self, id, name, city, school):
        self.id = id
        self.name = name
        self.city = city
        self.school = school

    def __str__(self) -> str:
        return f'Person id: {self.id}, name: {self.name}, city: {self.city}, school: {self.school}'

with open("resources/fixed-length/users.txt", "r") as f:
    users = f.read().splitlines()

userList = []
for user in users:
    userList.append(User(user[0:4].strip(),user[4:30].strip(),user[30:60].strip(),user[60:90].strip()))
    
    
for user in userList:
    print(user)
