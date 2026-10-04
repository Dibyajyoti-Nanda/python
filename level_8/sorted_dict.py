student = {
    "dengu":83,
    "hengu":79,
    "pengu":88,
    "deng":80
}

sorted_dict = dict(sorted(student.items(), key= lambda item:item[1]))

print(sorted_dict)