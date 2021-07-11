import json

#here we will try to parse content from json file

with open('courses.json') as f:
    dict_file = json.load(f)

    print(type(dict_file))

    print(dict_file)