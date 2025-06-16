import json
import os
import sys
from errors import *

# paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ast_path = os.path.join(script_dir, "ast.json")

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
    
def read(path):
    target_path = os.path.normpath(os.path.join(script_dir, path))
    contents = []

    try: 
        with open(target_path, "r") as f:
            lines = f.readlines()
            file_i = 0
            while file_i < len(lines):
                contents.append(lines[file_i].strip())
                file_i += 1
        return contents
    except FileNotFoundError:
        raise FileError(f"Could not find file {path}")
    
def crunch(arg_1, arg_2, op, forced_type=None):
            result = 0
            if op == '+':
                if forced_type == "string":
                    result = int(arg_1) + int(arg_2)
                    answer = str(result)
                    return answer
                elif forced_type == "bool":
                    result = int(arg_1) + int(arg_2)
                    if result != 0:
                        return True
                    elif result == 0:
                        return False
                elif forced_type == "char":
                    result = int(arg_1) + int(arg_2)
                    return chr(result)
                else:
                    return int(arg_1) + int(arg_2)
            elif op == '-':
                if forced_type == "string":
                    result = int(arg_1) - int(arg_2)
                    answer = str(result)
                    return answer
                elif forced_type == "bool":
                    result = int(arg_1) - int(arg_2)
                    if result != 0:
                        return True
                    elif result == 0:
                        return False
                elif forced_type == "char":
                    result = int(arg_1) - int(arg_2)
                    return chr(result)
                else:
                    return int(arg_1) - int(arg_2)
            elif op == '*':
                if forced_type == "string":
                    result = int(arg_1) * int(arg_2)
                    answer = str(result)
                    return answer
                elif forced_type == "bool":
                    result = int(arg_1) * int(arg_2)
                    if result != 0:
                        return True
                    elif result == 0:
                        return False
                elif forced_type == "char":
                    result = int(arg_1) * int(arg_2)
                    return chr(result)
                else:
                    return int(arg_1) * int(arg_2)
            elif op == '/':
                try:
                    if forced_type == "string":
                        result = int(arg_1) / int(arg_2)
                        answer = str(result)
                        return answer
                    elif forced_type == "bool":
                        result = int(arg_1) / int(arg_2)
                        if result != 0:
                            return True
                        elif result == 0:
                            return False
                    elif forced_type == "char":
                        result = int(arg_1) / int(arg_2)
                        return chr(int(result))
                    else:
                        return int(arg_1) / int(arg_2)
                except ZeroDivisionError:
                    raise ZeroCannotRuleTheWorld("You cannot divide zero by anything")
#endregion


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
                    x = val.keys()
                    if "index" in x:
                        if val["index"] in variables:
                            list_var = val["index"]
                            list_ = variables[list_var]
                            if type(list_) is list:
                                index = int(val["val"])
                                print(list_[index])
                    
                    if val["type"] == "read":
                        path = val["path"]
                        contents = read(path)
                        for line in contents:
                            print(line)

                    elif val["type"] == "crunch":
                        left = val["left"]
                        op = val["op"]
                        right = val["right"]
                        if "forced_type" in val.keys():
                            forced_type = val["forced_type"]
                            result = crunch(left, right, op, forced_type)
                            if result == True:
                                result = "true"
                            elif result == False:
                                result = "false"
                            print(result)
                        else:
                            result = crunch(left, right, op)
                            print(result)
                
                elif type(val) is list:
                    def current():
                        return final_list[spag_index]
                    spag_index = 0
                    final_list = []
                    while spag_index < len(val):
                        if val[spag_index] in variables:
                            var = variables[val[spag_index]]
                            final_list.append(var)
                            if type(var) is dict:
                                if var["type"] == "read":
                                    path = var["path"]
                                    contents = read(path)
                                    for line in contents:
                                        final_list.append(line)
                                if var["type"] == "crunch":
                                    left = var["left"]
                                    op = var["op"]
                                    right = var["right"]
                                    if "forced_type" in var.keys():
                                        forced_type = var["forced_type"]
                                        result = crunch(left, right, op, forced_type)
                                        if result == True:
                                            result = "true"
                                        elif result == False:
                                            result = "false"
                                        final_list.append(result)
                                    else:
                                        result = crunch(left, right, op)
                                        final_list.append(result)
                        
                        else:
                            final_list.append(val[spag_index])
                        spag_index += 1
                    for item in final_list:
                        if type(item) is dict:
                            final_list.remove(item)
                    print("".join(str(item) for item in final_list))           
                elif val in variables:
                    if variables[val] == True:
                        print("true")
                    elif variables[val] == False:
                        print("false")
                    elif type(variables[val]) is dict:
                        var = variables[val]
                        x = var.keys()
                        if "index" in x:
                            if var["index"] in variables:
                                list_var = var["index"]
                                list_ = variables[list_var]
                                if type(list_) is list:
                                    index = int(var["val"])
                                    print(list_[index])
                        if var["type"] == "read":
                            path = var["path"]
                            contents = read(path)
                            for line in contents:
                                print(line)
                        if var["type"] == "crunch":
                            left = var["left"]
                            op = var["op"]
                            right = var["right"]
                            if "forced_type" in var.keys():
                                forced_type = var["forced_type"]
                                result = crunch(left, right, op, forced_type)
                                if result == True:
                                    result = "true"
                                elif result == False:
                                    result = "false"
                                print(result)
                            else:
                                result = crunch(left, right, op)
                                print(result)
                        
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

