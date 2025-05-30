import json

with open("macro.json", "r") as f:
    file = json.load(f)
    for node in file:
        file.keys()