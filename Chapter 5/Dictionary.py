# Dictionary Basics

student= {
    "name": "Shubhangi Jaiswal",
    "city": "Motihari",
    "age":22,
    "rollNumber": 33
}
print(type(student))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"city":"lucknow"})
print(student)