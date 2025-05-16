import sys

args = sys.argv

if len(args) < 2:
    print("Usage: python3 parser.py <filename>")
    sys.exit(1)

# File name <filename>.itx MUST INCLUDE ITX
filename = args[1]

# Global Functions
def read(path):
        try:
            with open(path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: could not fine the file {path}"
        except Exception as e:
            return f"Error reading file: {str(e)}"

try:
    file = open(filename)

    # Storages
    variables = {}
    types = {}
    craft_args = {}
    answer = ""

    # Functions (In the FIle)
    def crunch(arg_1, arg_2, op, forced_type=None):
        result = 0
        if op == '+':
            if forced_type == "string":
                result = int(arg_1) + int(arg_2)
                answer = str(result)
                return answer
            else:
                return int(arg_1) + int(arg_2)
        elif op == '-':
            if forced_type == "string":
                result = int(arg_1) - int(arg_2)
                answer = str(result)
                return answer
            else:
                return int(arg_1) - int(arg_2)
        elif op == '*':
            if forced_type == "string":
                result = int(arg_1) * int(arg_2)
                answer = str(result)
                return answer
            else:
                return int(arg_1) * int(arg_2)
        elif op == '/':
            if forced_type == "string":
                result = int(arg_1) / int(arg_2)
                answer = str(result)
                return answer
            else:
                return int(arg_1) / int(arg_2)

    for line in file:
        input = line.strip()

        # Comment logic
        input = input.split("//")[0].strip()

        if not input:
            continue

        if input.endswith(';'):
            if input.count("declare") != 1 and input.count("=") == 1:
                craft_raw = input.split("=")
            try:    
                # DECLARE variable declaration --Integers
                if input.startswith("int declare"):
                    int_input = input[11:].strip().replace(';','')
                    name, value = int_input.split("=")
                    name = name.strip()
                    value = value.strip()
                    # Crunch insertion
                    if value.count("crunch"):
                        raw_crunch = value

                        func_name = raw_crunch[:raw_crunch.index("(")]
                        arg_string = raw_crunch[raw_crunch.index("(")+1 : -1]

                        raw_args = arg_string.split(",")
                        final_args = [argument.strip() for argument in raw_args]
                        fixed_args = []
                        for arg in final_args:
                            if arg.isdigit():
                                fixed_args.append(int(arg))
                            elif arg in variables:
                                fixed_args.append(variables[arg])
                            else:
                                fixed_args.append(arg)

                        crunch_result = crunch(fixed_args[0], fixed_args[1], fixed_args[2])
                        variables[name] = crunch_result
                    else:
                        variables[name] = value
                        types[name] = "int"
                # DECLARE --Strings
                elif input.startswith("string declare"):
                    raw_string = input[14:].strip().replace(';','')
                    name, value = raw_string.split("=")
                    name = name.strip()
                    value = value.strip().replace('"','')
                    # Crunch insertion
                    if value.count("crunch"):
                        raw_crunch = value

                        func_name = raw_crunch[:raw_crunch.index("(")]
                        arg_string = raw_crunch[raw_crunch.index("(")+1 : -1]

                        raw_args = arg_string.split(",")
                        final_args = [argument.strip() for argument in raw_args]
                        fixed_args = []
                        for arg in final_args:
                            if arg.isdigit():
                                fixed_args.append(int(arg))
                            elif arg in variables:
                                fixed_args.append(variables[arg])
                            else:
                                fixed_args.append(arg)
                        crunch_result = crunch(fixed_args[0], fixed_args[1], fixed_args[2], fixed_args[3])
                        variables[name] = crunch_result  
                    # read insertion
                    elif value.count("read"):
                        raw_read = value

                        func_name = raw_read[:raw_read.index("(")]
                        arg_string = raw_read[raw_read.index("(")+1 : -1]

                        read_result = read(arg_string)
                        variables[name] = read_result
                    else:
                        variables[name] = str(value)
                        types[name] = "string"
                # DECLARE --Booleans
                elif input.startswith("bool declare"):
                    raw = input[12:].strip().replace(';','')
                    name, value = raw.split("=")
                    name = name.strip()
                    value = value.strip()

                    if value.lower() == "true":
                        variables[name] = True
                        types[name] = "bool"
                    elif value.lower() == "false":
                        variables[name] = False
                        types[name] = "bool"
                    else:
                        print("Error: Invalid boolean")
                # DECLARE --Floats
                elif input.startswith("float declare"):
                    float_input = input[13:].strip().replace(';','')
                    name, value = float_input.split("=")
                    name = name.strip()
                    value = value.strip()
                    variables[name] = float(value)
                    types[name] = "float"
                # DECLARE --Char
                elif input.startswith("char declare"):
                    raw = input[12:].strip().replace(';','')
                    name, value = raw.split("=")
                    name = name.strip()
                    value = value.strip()
                    value = ord(value)
                    variables[name] = chr(value)
                    types[name] = "float"
            except (NameError, ValueError):
                print("Error: Declaration syntax incorrect")

            # OUTPUT print statement logic
            if input[:7].count("output") == 1:
                output_expr = input[7:].replace(';', '').strip()
                if output_expr.count("+") >= 1:
                    parts = output_expr.split(" + ")
                    result = ""

                    for part in parts:
                        part = part.strip().replace('"','')

                        if part in variables:
                            result += str(variables[part])
                        else:
                            result += part
                    print(result)
                elif output_expr.startswith('"'):
                    print(output_expr.replace('"',''))
                # Going past standard
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
            if input.count("=") == 1:
                input = input.split("=")
                if input[0].count("declare") != 1 or input[0].count("output") != 1:
                    name = input[0].strip()

        elif input.strip().endswith(';') != True: 
            print("Error: A semicolon was not found in this line")

except FileNotFoundError:
    print("Error: Intext file not found")