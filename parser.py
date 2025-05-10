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
            # DECLARE variable declaration --Integers
            if input[:11] == "int declare":
                int_input = input[11:].strip().replace(';','')
                name, value = int_input.split("=")
                name = name.strip()
                value = value.strip()
                variables[name] = int(value)
            # DECLARE --string
            elif input[:14] == "string declare":
                raw_string = input[14:].strip().replace(';','')
                name, value = raw_string.split("=")
                name = name.strip()
                value = value.strip().replace('"','')
                variables[name] = str(value)
            # DECLARE --booleans
            elif input[:12] == "bool declare":
                raw = input[12:].strip().replace(';','')
                name, value = raw.split("=")
                name = name.strip()
                value = value.strip()

                if value.lower() == "true":
                    variables[name] = True
                elif value.lower() == "false":
                    variables[name] = False
                else:
                    print("Error: Is that even a boolean?")

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
                else:
                    print("Error: What are you trying to say bub?")
        elif input.strip().endswith(';') != True: 
            print("Error: Where's your semicolon bro?")

except FileNotFoundError:
    print("Error: Intext file not found")