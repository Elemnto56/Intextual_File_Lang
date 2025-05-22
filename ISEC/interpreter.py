import json
import os

# paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ast_path = os.path.join(script_dir, "ast.json")

with open(ast_path, "r") as f:
    tree = json.load(f)

    # Storages
    types = {}
    variables = {}

    for node in tree:
        if node["type"] == "declare":
            name = node["var_name"]
            value = node["var_value"]
            typE = node["var_type"]

            if typE == "int":
                value = int(value)
            elif typE == "float":
                value = float(value)
            elif typE == "bool":
                if value.lower() == "true":
                    value = True
                else:
                    value = False
            elif typE == "char":
                value = value.replace("'","")
                value = ord(value)
                value = chr(value)

            variables[name] = value

            
        elif node["type"] == "output":
            val = node["value"]
            if val in variables:
                print(variables[val])
            else:
                print(val)

