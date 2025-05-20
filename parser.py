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
    lines = file.readlines()
    file_i = 0 


    # Storages
    variables = {}
    types = {}
    craft_args = {}
    answer = ""
    
    while file_i < len(lines):
        line = lines[file_i].strip()

        # Functions (In the File)
        def logic_engine(logic):
            return eval(logic)
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

        # Comment & blank logic
        line = line.split("//")[0].strip()
        
        if "" == line:
            file_i += 1
            continue

        if line.endswith(';'):
            # REPEAT loop logic
            if line.startswith("repeat") and line.endswith("{"):
                logic = line[6:line.index('{')].strip()
                repeat_lines = []
                file_i += 1
                while lines[file_i].strip() != "}":
                    repeat_lines.append(lines[file_i].strip())
                    file_i += 1
                while logic_engine(logic):
                    for rep_line in repeat_lines:
                        rep_line = rep_line.strip()
                        if rep_line.startswith("output"):
                            output_expr = rep_line[7:].replace(';', '').strip()
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
                            elif output_expr in variables:
                                if types[output_expr] == 'bool':
                                    print("true" if variables[output_expr] else "false")
                                else:
                                    print(variables[output_expr])
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
                file_i += 1
                continue

            if line.count("declare") == 1 and line.count("=") == 1:
                try:    
                    # DECLARE variable declaration --Integers
                    if line.startswith("int declare"):
                        int_line = line[11:].strip().replace(';','')
                        name, value = int_line.split("=")
                        name = name.strip()
                        value = value.strip()
                        # Crunch insertion
                        if value.count("crunch"):
                            raw_crunch = value

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
                    elif line.startswith("string declare"):
                        raw_string = line[14:].strip().replace(';','')
                        name, value = raw_string.split("=")
                        name = name.strip()
                        value = value.strip().replace('"','')
                        # Crunch insertion
                        if value.count("crunch"):
                            raw_crunch = value

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

                            arg_string = raw_read[raw_read.index("(")+1 : -1]

                            read_result = read(arg_string)
                            variables[name] = read_result
                        else:
                            variables[name] = str(value)
                            types[name] = "string"
                    # DECLARE --Booleans
                    elif line.startswith("bool declare"):
                        raw = line[12:].strip().replace(';','')
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
                    elif line.startswith("float declare"):
                        float_line = line[13:].strip().replace(';','')
                        name, value = float_line.split("=")
                        name = name.strip()
                        value = value.strip()
                        variables[name] = float(value)
                        types[name] = "float"
                    # DECLARE --Char
                    elif line.startswith("char declare"):
                        raw = line[12:].strip().replace(';','')
                        name, value = raw.split("=")
                        name = name.strip()
                        value = value.strip()
                        value = ord(value)
                        variables[name] = chr(value)
                        types[name] = "float"
                except (NameError, ValueError):
                    print("Error: Declaration syntax incorrect")

            # OUTPUT print statement logic
            if line.startswith("output"):
                output_expr = line[7:].replace(';', '').strip()
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
                    if types[output_expr] == 'bool':
                        if variables[output_expr] == True:
                            value = "true"
                            variables[output_expr] = value
                        elif variables[output_expr] == False:
                            value = "false"
                            variables[output_expr] = value
                    else:
                        print(variables[output_expr])
                elif line.startswith("declare"):
                    print("")
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

        elif not line.strip().endswith(';') and not line.strip().endswith('{') and not line.strip().endswith('}'):
            print("Error: A semicolon was not found in this line")
        file_i = file_i + 1

except FileNotFoundError:
    print("Error: Intext file not found")