student = {
    "dengu":83,
    "hengu":82,
    "pengu":88,
    "deng":80
}

max_key = max(student,key=student.get)

print(f"maximum key {max_key}")
print(f"maximum value {student[max_key]}")