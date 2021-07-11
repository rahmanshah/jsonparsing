import json

courses = '{"name": "Shah Rahman","Courses": [ "Java", "Python"]}'

#Loads methonds parse json strings and returns dictionary

dict_courses = json.loads(courses)

print(type(dict_courses))

print(dict_courses)

print(dict_courses["name"])

print(dict_courses["Courses"])

print(dict_courses["Courses"][0])

print(dict_courses["Courses"][1])