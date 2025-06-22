import sys
import json
import os
from errors import LexerError

args = sys.argv

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "tokens.json")



if len(args) < 2:
    print("Usage: python3 parser.py <filename>")
    sys.exit(1)

filename = args[1]

with open(filename, 'r') as file:
    lines = file.readlines()
    index = 0

    # Where tokens are stored
    all_tokens = []

    while index < len(lines):
        line = lines[index].strip()

        if "//" in line:
            line = line.split("//")[0].strip()
        
        if line.isspace():
            index += 1
            continue

        i = 0
        while i < len(line):

            # if line is a space
            if line[i].isspace():
                i += 1
                continue

            if line[i] in [";", "="]:
                all_tokens.append({'type': 'SYMBOL', 'value': line[i]})
                i += 1
                continue

            if line[i:i+2] == "->":
                all_tokens.append({"type": "ARROW", "value": line[i:i+2]})
                i += 2
                continue

            if line[i] in ["+", "-", "*", "/"]:
                all_tokens.append({"type": "OPERATOR", "value": line[i]})
                i += 1
                continue
            
            # If line is a word
            if line[i].isalpha():
                ident = ''
                while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                    ident += line[i]
                    i += 1
                if ident in ["bool", "string", "int", "char", "float", "output", "declare", "ord", "order"]:
                    all_tokens.append({'type': 'KEYWORD', 'value': ident})
                elif ident == "true" or ident == "false":
                    all_tokens.append({"type": "BOOL", "value": ident})
                else:
                    all_tokens.append({'type': 'IDENTIFIER', 'value': ident})
                continue

            # Detech right bracket for Order    
            if line[i] == "[":
                all_tokens.append({"type": "LBRACKET", "value": line[i]})
                i += 1
                continue

            if line[i] == ",":
                all_tokens.append({"type": "COMMA", "value": line[i]})
                i += 1
                continue

            if line[i] == "]":
                all_tokens.append({"type": "RBRACKET", "value": line[i]})
                i += 1
                continue

            if line[i] == "'":
                if i + 2 < len(line) and line[i + 2] == "'":
                    char = line[i + 1]
                    all_tokens.append({"type": "CHAR", "value": char})
                    i += 3
                    continue
            
            if line[i] == "(":
                all_tokens.append({"type": "LPARA", "value": line[i]})
                i += 1
                continue

            if line[i] == ")":
                all_tokens.append({"type": "RPARA", "value": line[i]})
                i += 1
                continue

            if line[i:i+3] == "<<<":
                i += 3
                block_val = ""

                index += 1
                while index < len(lines):
                    if ">>>" in lines[index]:
                        break
                    block_val += lines[index].strip() + "\n"
                    index += 1

                all_tokens.append({"type": "BLOC", "value": block_val})
                continue

            # If line is a number
            if line[i].isdigit():
                num = ''
                while i < len(line) and (line[i].isdigit() or line[i] == "."):
                    num += line[i]
                    i += 1
                all_tokens.append({'type': 'INT', 'value': num})
                continue

            # If line is a string
            if line[i] in ['"']:
                i += 1
                string_val = ''

                while i < len(line):
                    if line[i] in ['"']:
                        break
                    string_val += line[i]
                    i += 1
                i += 1

                if i >= len(line):
                    raise LexerError(f"String ranged out on line {index + 1}. Did you forget a breaker?")
                

                all_tokens.append({'type': 'STRING', 'value': string_val})
                continue

            raise LexerError(f"Illegal character {line[i]!r} on line {index + 1}")

        index += 1    

        with open(output_path, "w") as out_file:
            json.dump(all_tokens, out_file, indent=2)