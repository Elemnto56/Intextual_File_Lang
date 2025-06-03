import json
import os
import sys
from errors import InvalidNode, MissingBreaker, clean_exit_hook, RangeException

#region Functions
def interpret(node):
    if node.get("type") == "declare":
        keys = ["var_name", "var_type", "var_value"]
        for key in keys:
            if key not in node:
                raise InvalidNode(f"Missing argument {key} for declare in node: \n{json.dumps(node, indent=2)}")

        name = node["var_name"]
        value = node["var_value"]
        type_ = node["var_type"]

        if type_ == "int":
            value = int(value)
        elif type_ == "float":
            value = float(value)
        elif type_ == "bool":
            if value.lower() == "true":
                value = True
            else:
                value = False
        elif type_ == "char":
            value = value.replace("'","")
            value = ord(value)
            value = chr(value)
        elif type_ == "string":
            value = str(value)
        elif type_ not in valid_types:
            raise InvalidNode(f"Invalid type: \"{type_}\" in node: \n{json.dumps(node, indent=2)}")

        variables[name] = value
    
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
    
    elif node.get("type") == "if":
            allowed_ops = {
                "==": lambda a, b: a == b,
                "!=": lambda a, b: a != b,
                ">": lambda a, b: a > b,
                "<": lambda a, b: a < b,
                ">=": lambda a, b: a >= b,
                "<=": lambda a, b: a <= b
            }


            logic = dict(node["condition"])

            # Unpack
            left = logic["left"]
            right = logic["right"]
            op = logic["operator"]

            body = node["body"]

            for sub_node in body:
                if op in allowed_ops:
                    result = eval(f"{allowed_ops[op](left, right)}")
                else:
                    raise InvalidNode(f"Unsupported operator: {op}")
                
                if result:
                    interpret(sub_node)
        
    elif node.get("type") not in ["declare", "output", "if"] and "semicolon" not in node:
            raise InvalidNode(f"Invalid sytax node \n{json.dumps(node, indent=2)}")
#endregion

# paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ast_path = os.path.join(script_dir, "ast.json")

with open(ast_path, "r") as f:
    tree = json.load(f)

    # indexs
    i = 0

    # Storages
    valid_types = ["int", "float", "char", "bool", "string", "order", "ord"]
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
            type_ = node["var_type"]

            if type_ == "int":
                value = int(value)
            elif type_ == "float":
                value = float(value)
            elif type_ == "bool":
                if value.lower() == "true":
                    value = True
                else:
                    value = False
            elif type_ == "char":
                value = value.replace("'","")
                value = ord(value)
                value = chr(value)
            elif type_ == "string":
                value = str(value)
            elif type_ == "ord" or type_ == "order":
                variables[name] = list(value)
            elif type_ == "void":
                variables[name] = value
            elif type_ not in valid_types:
                raise InvalidNode(f"Invalid type: \"{type_}\" in node: \n{json.dumps(node, indent=2)}")

            if i + 1 >= len(tree) or "semicolon" not in tree[i + 1]:
                raise MissingBreaker(f"No semicolon found at AST node or line of Intext \n{json.dumps(node, indent=2)}\n ^ Missing here\n---Or on this line---\n {type_} declare {name} = {value} <-- Here")

            variables[name] = value

            
        elif node.get("type") == "output":
            val = node["value"]

            if i + 1 >= len(tree) or "semicolon" not in tree[i + 1]:
                raise MissingBreaker(f"No semicolon found at AST node or line of Intext \n{json.dumps(node, indent=2)}\n ^ Missing here\n---Or on this line---\n output {val} <-- Here")

            try:
                if type(val) is dict:
                    if val["index"] in variables:
                        list_var = val["index"]
                        list_ = variables[list_var]
                        if type(list_) is list:
                            index = int(val["val"])
                            print(list_[index])
            
                elif val in variables:
                    if variables[val] == True:
                        print("true")
                    elif variables[val] == False:
                        print("false")
                    elif type(variables[val]) is dict:
                        var = variables[val]
                        if var["index"] in variables:
                            list_var = var["index"]
                            list_ = variables[list_var]
                            if type(list_) is list:
                                index = int(var["val"])
                                print(list_[index])
                    else:
                        print(variables[val])
                else:
                    print(val)
            except IndexError:
                raise RangeException(f"Range exceeded the bounds of the indexed order \n {json.dumps(variables[val], indent=2)}")

        elif node.get("type") == "if":
            allowed_ops = {
                "==": lambda a, b: a == b,
                "!=": lambda a, b: a != b,
                ">": lambda a, b: a > b,
                "<": lambda a, b: a < b,
                ">=": lambda a, b: a >= b,
                "<=": lambda a, b: a <= b
            }


            logic = dict(node["condition"])

            # Unpack
            left = logic["left"]
            right = logic["right"]
            if left in variables:
                left = variables[left]
            if right in variables:
                right = variables[right]
            op = logic["operator"]

            body = node["body"]

            for sub_node in body:
                if op in allowed_ops:
                    result = eval(f"{allowed_ops[op](left, right)}")
                else:
                    raise InvalidNode(f"Unsupported operator: {op}")
                
                if result:
                    interpret(sub_node)
        
        elif node.get("comment"):
            continue
            
            
        elif node.get("type") not in ["declare", "output", "if"] and "semicolon" not in node:
            raise InvalidNode(f"Invalid sytax node \n{json.dumps(node, indent=2)}")

