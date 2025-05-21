import sys
args = sys.argv

# Exceptions
class LexerError(Exception):
    pass

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
        
        i = 0
        while i < len(line):
            if line[i].isspace():
                i += 1
                continue
            
            if line[i].isalpha():
                ident = ''
                while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                    ident += line[i]
                    i += 1
                if ident in ["bool", "string", "int", "char", "float", "output"]:
                    all_tokens.append({'type': 'KEYWORD', 'value': ident})
                else:
                    all_tokens.append({'type': 'IDENTIFIER', 'value': ident})
                i += 1
                continue
            if line[i].isdigit():
                num = ''
                while i < len(line) and line[i].isdigit():
                    num += line[i]
                    i += 1
                all_tokens.append({'type': 'INT', 'value': num})
                i += 1
                continue
            if line[i] in ['"']:
                i += 1
                string_val = ''

                while i < len(line):
                    if line[i] in ['"']:
                        break
                    string_val += line[i]
                    i += 1

                if i >= len(line):
                    raise LexerError(f"Unterminated string on line {index + 1}")

                i += 1  # Skip closing quote
                all_tokens.append({'type': 'STRING', 'value': string_val})
                continue

            if line[i] in ['=', ';']:
                all_tokens.append({'type': 'SYMBOL', 'value': line[i]})
                i += 1
                continue
            
            i += 1
            raise LexerError(f"Illegal character {line[i]!r} on line {index + 1}")
        
        # Comment and whitespace checks (Outer Loop)
        if not line:
            continue
        if "//" in line:
            line = line.split("//")[0].strip()

    for token in all_tokens:
        print(token)