student={
    "name": "Deepthi",
    "age": 20,
    "Course" : "Python"
}
print(student)
print(student['name'])
print(student['age'])
print(student['Course'])
print(student.keys())
print(student.values())
print(student.items())
#to get a value using key
print(student.get('name'))
student.update({'age':21})
student.pop("Course")
print(student)