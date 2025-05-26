import json
import os

class MissingBreaker(Exception):
    pass

# paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ast_path = os.path.join(script_dir, "ast.json")

with open(ast_path, "r") as f:
    tree = json.load(f)

    # indexs
    i = 0

    # Storages
    types = {}
    variables = {}

    for i, node in enumerate(tree):
        if node.get("type") == "declare":

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

            if i + 1 >= len(tree) or "semicolon" not in tree[i + 1]:
                raise MissingBreaker()

            
        elif node.get("type") == "output":
            val = node["value"]
            if val in variables:
                print(variables[val])
            else:
                print(val)

            if i + 1 >= len(tree) or "semicolon" not in tree[i + 1]:
                raise MissingBreaker("No semicolon was found at the end of this statement")

