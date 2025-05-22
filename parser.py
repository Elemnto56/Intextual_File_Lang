import json
import sys

with open("tokens.json", "r") as f:
    tokens = json.load(f)

    index = 0
    ast = []

    # Fuctions
    # Grab token and move along
    def current():
        return tokens[index] if index < len(tokens) else None
    
    # Advance index
    def advance():
        global index
        index += 1
    
    while index < len(tokens):
        token = current()

        if token["type"] == "KEYWORD" and token["value"] in ["output"]:
            advance()
            token = current()

            if token["type"] == "IDENTIFIER":
                name = token["value"]
                ast.append({
                    "type": "output",
                    "value": name
                })
            elif token["type"] in ["INT", "FLOAT", "CHAR", "BOOL", "STRING"]:
                literal = token["value"]
                ast.append({
                    "type": "output",
                    "value": literal
                })

            advance()
            continue                            
        
        # Check for intial keywords/indentifiers 
        if token["type"] == "KEYWORD" and token["value"] in ["int", "float", "char", "bool", "string"]:
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
            
        with open("ast.json", "w") as out_file:
            json.dump(ast, out_file, indent=2)
            sys.exit(0)
