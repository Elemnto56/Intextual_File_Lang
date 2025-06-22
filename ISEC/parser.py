import json
import os
import time
from errors import RangeException, MissingBreaker, TypeMismatch

#region paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ast_path = os.path.join(script_dir, "ast.json")
tokens_path = os.path.join(script_dir, "tokens.json")
#endregion

with open(tokens_path, "r") as f:
    tokens = json.load(f)

    index = 0
    ast = []

    # Fuctions
    # Grab token and move along
    def current():
        if index >= len(tokens):
            raise RangeException("Unexpected end")
        return tokens[index]
    
    # Advance index
    def advance():
        global index
        index += 1

    while index < len(tokens):
        token = current()

        if token["type"] == "KEYWORD":
            if token["value"] in ["int", "float", "char", "bool", "string", "ord", "order"]:
                var_type = token["value"]
                advance()
                token = current()

                # After the intial keywords/indents, check the ones after them, if any [DECLARE ROUTE]
                if token["type"] == "KEYWORD" and token["value"] in ["declare"]:
                    advance()
                    token = current()

                    # Check if it's a variable [DECLARE]
                    if token["type"] == "IDENTIFIER":
                        var_name = token["value"]
                        advance()
                        token = current()

                        # Make sure the equal sign is being used for assignment [DECLARE]
                        if token["type"] == "SYMBOL" and token["value"] in ["="]:
                            advance()
                            token = current()
                            items = []

                            if token["type"] == "LBRACKET" and token["value"] == "[":
                                advance()
                                while True:
                                    tok = current()
                                    if tok is None:
                                        raise MissingBreaker("List too long; didn't see ']")
                                    
                                    if tok["type"] in ["INT", "FLOAT", "CHAR", "BOOL", "STRING"]:
                                        items.append(tok["value"])
                                        advance()
                                        continue

                                    if tok["type"] == "COMMA" and tok["value"] == ",":
                                        advance()
                                        continue

                                    if tok["type"] == "RBRACKET" and tok["value"] == "]":
                                        advance()
                                        break
                                        
                                        
                                    raise MissingBreaker(f"Expected a comma or closing bracket, got {tok!r} instead")
                            
                                var_value = items
                                
                                ast.append({
                                    "type": "declare",
                                    "var_type": var_type,
                                    "var_name": var_name,
                                    "var_value": var_value
                                })


                            # Check what type of thing the variable is being assigned to [DECLARE]
                            if token["type"] in ["INT", "FLOAT", "CHAR", "BOOL", "STRING"]:
                                
                                var_value = token["value"]
                                ast.append({
                                    "type": "declare",
                                    "var_type": var_type,
                                    "var_name": var_name,
                                    "var_value": var_value
                                })
                                advance()
                                

            elif token["value"] == "output":
                name = ""
                advance()            
                token = current()
                if token["type"] in ["INT", "FLOAT", "CHAR", "BOOL", "STRING", "IDENTIFIER"]:
                    name = token["value"]  
                    advance()              
                    token = current()

                    if token["type"] == "OPERATOR":
                        advance()
                        token = current()
                        if token["type"] in ["INT", "FLOAT", "CHAR", "BOOL", "STRING", "IDENTIFIER"]:
                            spaghetti_list = [name, token["value"]]
                            new_tok = tokens[index + 1]
                            if new_tok["type"] == "OPERATOR" and new_tok["value"] == "+":
                                advance()
                                while True:

                                    if new_tok["type"] == "OPERATOR" and new_tok["value"] == "+":
                                        advance()
                                        new_tok = current()

                                    if new_tok["type"] in ["INT", "FLOAT", "CHAR", "BOOL", "STRING", "IDENTIFIER"]:
                                        val = new_tok["value"]

                                        spaghetti_list.append(val)
                                        advance()
                                        new_tok = current()

                                    if new_tok["value"] == ";":
                                        break
                                        
                                ast.append({
                                    "type": "output",
                                    "value": spaghetti_list
                                })

            
                            else:
                                ast.append({
                                    "type": "output",
                                    "value": spaghetti_list
                                })
                                advance()


                    elif token["type"] == "LBRACKET":
                        advance()          
                        token = current()  
                        val = token["value"]
                        advance()         
                        token = current()

                        if token["type"] == "RBRACKET":
                            advance() 

                        ast.append({
                            "type": "output",
                            "value": {
                                "index": name,
                                "val": val
                            }
                        })
                    
                    elif token["type"] == "LPARA":
                        advance()
                        token = current()
                        if token["type"] == "STRING":
                            path = token["value"]
                            advance()
                            token = current()
                            if token["type"] == "RPARA":
                                ast.append({
                                    "type": "output",
                                    "value": {
                                        "type": "read",
                                        "path": path
                                    }
                                })
                                advance()
                                token = current()
                                if token["type"] == "OPERATOR" and token["value"] == "+":
                                    raise TypeMismatch()
                        elif token["type"] in ["INT", "FLOAT"]:
                            left = token["value"]
                            advance()
                            advance() # Skip COMMA
                            token = current()
                            if token["type"] in ["INT", "FLOAT"]:
                                right = token["value"]
                                advance()
                                advance()
                                token = current()
                                if token["type"] == "OPERATOR":
                                    op = token["value"]
                                    advance()
                                    token = current()
                                    if token["type"] == "COMMA":
                                        advance()
                                        token = current()
                                        forced_type = token["value"]
                                        advance()
                                        token = current()
                                        if token["type"] == "RPARA":
                                            ast.append({
                                                "type": "output",
                                                "value": {
                                                    "type": "crunch",
                                                    "left": left,
                                                    "op": op,
                                                    "right": right,
                                                    "forced_type": forced_type
                                                } 
                                            })
                                            advance()
                                            token = current()
                                            if token["type"] == "OPERATOR" and token["value"] == "+":
                                                raise TypeMismatch()
                                    elif token["type"] == "RPARA":
                                        ast.append({
                                            "type": "output",
                                            "value": {
                                                "type": "crunch",
                                                "left": left,
                                                "op": op,
                                                "right": right
                                            }
                                        })
                                        advance()
                    
                    else:
                        ast.append({
                            "type": "output",
                            "value": name
                        })

                elif token["type"] == "BLOC":
                    contents = token["value"]
                    ast.append({
                        "type": "output",
                        "value": contents
                    })

                   
                '''      
                elif token["type"] in ["INT", "FLOAT", "CHAR", "BOOL", "STRING", "IDENTIFIER"]:
                    first = token["value"]
                    spaghetti_list = [name]
                    new_tok = tokens[index + 1]
                    if new_tok["type"] == "OPERATOR" and new_tok["value"] == "+":
                        advance()
                        while True:
                            if new_tok["type"] == "OPERATOR" and new_tok["value"] == "+":
                                advance()
                                new_tok = current()

                                if new_tok["type"] in ["INT", "FLOAT", "CHAR", "BOOL", "STRING", "IDENTIFIER"]:
                                    val = new_tok["value"]

                                    spaghetti_list.append(val)
                                    advance()
                                    new_tok = current()
                                
                                if new_tok["type"] == "SYMBOL" and new_tok["value"] == ";":
                                    break

                        ast.append({
                            "type": "output",
                            "value": spaghetti_list
                        })    
                    else:
                        literal = token["value"]
                        ast.append({
                            "type": "output",
                            "value": literal
                        })
                        advance()
                '''

            elif token["value"] == "declare":
                advance()
                token = current()
                if token["type"] == "IDENTIFIER":
                    name = token["value"]
                    advance()
                    token = current()
                    if token["type"] == "SYMBOL":
                        advance()
                        token = current()
                        if token["type"] in ["INT", "BOOL", "FLOAT", "CHAR", "STRING"]:
                            list_name = token["value"]
                            advance()
                            token = current()
                            ast.append({
                                "type": "declare",
                                "var_type": "void",
                                "var_name": name,
                                "var_value": list_name
                            })
                            token = current()
                        elif token["type"] == "IDENTIFIER" and token["value"] == "read":
                            advance()
                            token = current()
                            if token["type"] == "LPARA":
                                advance()
                                token = current()
                                if token["type"] == "STRING":
                                    path = token["value"]
                                    ast.append({
                                        "type": "declare",
                                        "var_type": "void",
                                        "var_name": name,
                                        "var_value": {
                                            "type": "read",
                                            "path": path
                                        }
                                    })
                                    advance()
                                    token = current()
                                    if token["type"] == "RPARA":
                                        advance()
                                else:
                                    raise TypeMismatch()
                        elif token["type"] == "IDENTIFIER" and token["value"] == "crunch":
                            advance()
                            advance() # Skip LPARA
                            token = current()
                            left = token["value"]
                            advance()
                            advance()
                            token = current()
                            if token["type"] in ["INT", "FLOAT"]:
                                right = token["value"]
                                advance()
                                advance()
                                token = current()
                                if token["type"] == "OPERATOR":
                                    op = token["value"]
                                    advance()
                                    token = current()
                                    if token["type"] == "COMMA":
                                        advance()
                                        token = current()
                                        forced_type = token["value"]
                                        ast.append({
                                           "type": "declare",
                                           "var_type": "void",
                                           "var_name": name, 
                                           "var_value": {
                                               "type": "crunch",
                                               "left": left,
                                               "op": op,
                                               "right": right,
                                               "forced_type": forced_type
                                           } 
                                        })
                                        advance()
                                        advance()
                                    elif token["type"] == "RPARA":
                                        ast.append({
                                            "type": "declare",
                                            "var_type": "void",
                                            "var_name": name,
                                            "var_value": {
                                                "type": "crunch",
                                                "left": left,
                                                "op": op,
                                                "right": right
                                            }
                                        })
                                        advance()
                        elif token["type"] == "IDENTIFIER" and token["value"] == "input":
                            advance()
                            token = current() 
                            advance() # Skip LPARA
                            token = current()
                            if token["type"] == "STRING":
                                newline = True
                                advance()
                                token = current()
                                advance() # Skip RPARA
                                token = current()
                                advance() # Skip ARROW
                                token = current()
                                if token["type"] == "STRING":
                                    prompt = token["value"]
                                    ast.append({
                                        "type": "declare",
                                        "var_type": "void:input",
                                        "var_name": name,
                                        "var_value": {
                                            "type": "input",
                                            "prompt": prompt,
                                            "newline": True
                                        }
                                    })
                                    advance()
                                else:
                                    raise TypeMismatch()
                            else:
                                advance() # Skip RPARA
                                token = current()
                                advance() # Skip ARROW
                                token = current()
                                if token["type"] == "STRING":
                                    prompt = token["value"]
                                    ast.append({
                                        "type": "declare",
                                        "var_type": "void:input",
                                        "var_name": name,
                                        "var_value": {
                                            "type": "input",
                                            "prompt": prompt,
                                            "newline": False
                                        }
                                    })
                                    advance()
                                else:
                                    raise TypeMismatch()

                        elif token["type"] == "BLOC":
                            contents = token["value"]
                            ast.append({
                                "type": "declare",
                                "var_type": "void",
                                "var_name": name,
                                "var_value": contents
                            })
                            advance()
                        else:
                            raise TypeError()
        if token["type"] == "IDENTIFIER":
            if token["value"] == "write":
                advance()
                token = current()
                if token["type"] == "LPARA" and token["value"] == "(":
                    advance()
                    token = current()
                    if token["type"] in ["STRING", "IDENTIFIER"]:
                        file = token["value"]
                        advance()
                        token = current() # Skip COMMA
                        advance()
                        token = current()
                        if token["type"] in ["STRING", "IDENTIFIER"]:
                            contents = token["value"]
                            contents = contents.encode().decode("unicode_escape")
                            advance()
                            token = current()
                            if token["type"] == "RPARA":
                                ast.append({
                                    "type": "write",
                                    "file": file,
                                    "contents": contents
                                })
                                advance()
                        else:
                            raise TypeMismatch()  
                    else:
                        raise TypeMismatch()
            
            elif token["value"] == "append":
                advance()
                token = current()
                if token["type"] == "LPARA" and token["value"] == "(":
                    advance() # Skip LPARA
                    token = current()
                    if token["type"] in ["STRING", "IDENTIFIER"]:
                        file = token["value"]
                        advance()
                        token = current()
                        advance() # Skip COMMA
                        token = current()
                        if token["type"] in ["STRING", "IDENTIFIER"]:
                            contents = token["value"]
                            contents = contents.encode().decode("unicode_escape")
                            advance()
                            token = current()
                            if token["type"] == "RPARA":
                                ast.append({
                                    "type": "append",
                                    "file": file,
                                    "additions": contents 
                                })
                                advance()
                            else:
                                raise TypeMismatch()
                    else:
                        raise TypeMismatch()
                
            elif token["value"] == "del" or token["value"] == "remove":
                advance()
                token = current()
                if token["type"] == "LPARA":
                    advance() # Skip LPARA

                    new_tok = current()
                    files = []
                    while True:
                        if new_tok["type"] == "STRING":
                            files.append(new_tok["value"])
                            advance()
                            new_tok = current()
                        
                        if new_tok["type"] == "COMMA":
                            advance()
                            new_tok = current()

                        if new_tok["type"] == "RPARA":
                            break
                    ast.append({
                        "type": "remove",
                        "value": files
                    })
                    advance()

        if token["type"] in ["SYMBOL", "BLOC"]:
            end_semi = token["value"]
            if token["value"] != ";":
                ast.append({
                    "breaker": "end_line"
                })
            else:
                ast.append({
                    "semicolon": end_semi
                })
                advance()
            
    with open(ast_path, "w") as out_file:
        json.dump(ast, out_file, indent=2)
            
