import sys

args = sys.argv

if len(args) < 2:
    print("Usage: python3 parser.py <filename>")
    sys.exit(1)

# File name <filename>.itx MUST INCLUDE ITX
filename = args[1]

try:
    file = open(filename)
    variables = {}
    for line in file:
        input = line.strip()
        if input.startswith("//"): # // Shalll be the comments
            continue

        if not input:
            continue

        if input[7:].endswith(';'):
            try:    
                # DECLARE variable declaration --Integers
                if input.startswith("int declare"):
                    int_input = input[11:].strip().replace(';','')
                    name, value = int_input.split("=")
                    name = name.strip()
                    value = value.strip()
                    variables[name] = int(value)
                # DECLARE --string
                elif input.startswith("string declare"):
                    raw_string = input[14:].strip().replace(';','')
                    name, value = raw_string.split("=")
                    name = name.strip()
                    value = value.strip().replace('"','')
                    variables[name] = str(value)
                # DECLARE --booleans
                elif input.startswith("bool declare"):
                    raw = input[12:].strip().replace(';','')
                    name, value = raw.split("=")
                    name = name.strip()
                    value = value.strip()

                    if value.lower() == "true":
                        variables[name] = True
                    elif value.lower() == "false":
                        variables[name] = False
                    else:
                        print("Error: Invalid boolean")
            except (NameError, ValueError):
                print("Error: Declaration syntax incorrect")

                variables[name] = value
            # OUTPUT print statement logic
            if input[:7].count("output") == 1:
                output_expr = input[7:].replace(';', '').strip()
                if output_expr.startswith('"') and output_expr.endswith('"'):
                    print(output_expr.replace('"',''))
                elif output_expr in variables:
                    print(variables[output_expr])
                elif input.count("declare") == 1:
                    continue
                elif output_expr == "true" or output_expr == "false":
                    print(output_expr)
                elif output_expr.isdigit():
                    print(output_expr)
                else:
                    try:
                        result = eval(output_expr, {"__builtins__": None}, variables)
                        print(result)
                    except Exception:
                        print("Error: Incorrect syntax for output")
                        
        elif input.strip().endswith(';') != True: 
            print("Error: A semicolon was not found in this line")

except FileNotFoundError:
    print("Error: Intext file not found")