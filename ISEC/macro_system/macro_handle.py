import json

with open("macro.json", "r") as f:
    file = json.load(f)
    index = 0
    while index < len(file):
        node = file[index]
        print(node)
        index += 1