import sys

args = sys.argv

if len(args) < 2:
    print("Usage: python3 parser.py <filename>")
    sys.exit(1)

# File name <filename>.itx MUST INCLUDE ITX
filename = args[1]

try:
    file = open(filename)
    for line in file:
        input = line.strip()
        if input.startswith("//"): # // Shalll be the comments
            continue

        #print("DEBUG: " + input)

        types = ["int", "string", "bool"]
        variables = {}

        if input[7:].endswith(';'):
            if input[:11] == "int declare":
                int_input = input[11:].strip().replace(';','')
                name, value = int_input.split("=")
                name.split()
                value.split()
                variables[name] = int(value)
            
            output_expr = input[7:].replace(';', '').strip()

            print(variables)

            if output_expr.startswith('"') and output_expr.endswith('"'):
                print(output_expr.replace('"',''))
            elif output_expr in variables:
                print(variables[output_expr])
            elif input.count("declare") == 1:
                continue
            else:
                print("Error: What are you trying to say bub?")
        elif input.endswith(';') != True: 
            print("Error: Where's your semicolon bro?")

except FileNotFoundError:
    print("Error: Intext file not found")