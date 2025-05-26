import json
import os
import sys


#region Errors
class MissingBreaker(Exception):
    pass

class InvalidNode(Exception):
    pass

def clean_exit_hook(exc_type, exc_value, _):
    if exc_type.__name__ in ["InvalidNode", "MissingBreaker"]:
        print(f"\033[1;35m{exc_type.__name__}:\033[0;35m {exc_value}\033[0m")
    else:
        sys.__excepthook__(exc_type, exc_value, _)

sys.excepthook = clean_exit_hook
#endregion

# paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ast_path = os.path.join(script_dir, "ast.json")

with open(ast_path, "r") as f:
    tree = json.load(f)

    # indexs
    i = 0

    # Storages
    valid_types = ["int", "float", "char", "bool", "string"]
    types = {}
    variables = {}

    for i, node in enumerate(tree):
        if node.get("type") == "declare":
            keys = ["var_name", "var_type", "var_value"]
            for key in keys:
                if key not in node:
                    raise InvalidNode(f"Missing argument {key} for declare in node: \n{json.dumps(node, indent=2)}")

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
            elif typE == "string":
                value = str(value)
            elif typE not in valid_types:
                raise InvalidNode(f"Invalid type: \"{typE}\" in node: \n{json.dumps(node, indent=2)}")

            variables[name] = value

            if i + 1 >= len(tree) or "semicolon" not in tree[i + 1]:
                raise MissingBreaker(f"No semicolon found at AST node \n{json.dumps(node, indent=2)}\n ^ Missing here")

            
        elif node.get("type") == "output":
            val = node["value"]
            if val in variables:
                if variables[val] == True:
                    print("true")
                elif variables[val] == False:
                    print("false")
                else:
                    print(variables[val])
            else:
                print(val)

            if i + 1 >= len(tree) or "semicolon" not in tree[i + 1]:
                raise MissingBreaker(f"No semicolon found at AST node \n{json.dumps(node, indent=2)}\n ^ Missing here")
        
        elif node.get("type") not in ["declare", "output"] and "semicolon" not in node:
            raise InvalidNode(f"Invalid sytax node \n{json.dumps(node, indent=2)}")

