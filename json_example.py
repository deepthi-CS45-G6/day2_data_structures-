#json dumps
import json
student = {
    "name": "Deepthi",
    "age": 21
}
json_data = json.dumps(student)
print(json_data)
#json loads
import json
student = {
    "name": "Deepthi",
    "age": 21
}
json_data = json.dumps(student)
print(json_data)
#json dump
import json
student = {
    "name": "Deepthi",
    "age": 21
}
with open("student.json", "w") as file:
    json.dump(student, file)
#json load
import json
with open("student.json", "r") as file:
    data = json.load(file)
print(data)