import re
import sys
import os
import subprocess

#region paths
root = os.path.dirname(os.path.abspath(__file__))
boot_file = os.path.join(root, "ISEC", "boot.py")
#endregion

def run_inspect(source_code: str):
    errors = []
    declared_vars = {}
    lines = source_code.splitlines()

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        if not stripped or stripped.startswith("//"):  # skip empty lines & comments
            continue

        if not stripped.endswith(";"):
            errors.append(f"Line {idx}: Missing semicolon. \n {stripped} <-")

        # Handle declare
        if stripped.startswith("declare "):
            match = re.match(r"declare\s+(\w+)\s*=\s*(.+);", stripped)
            if not match:
                errors.append(f"Line {idx}: Invalid declare syntax. \n {stripped} <-")
                continue
            varname = match.group(1)
            if varname in declared_vars:
                original_line = declared_vars[varname]
                errors.append(
                    f"Line {idx}: Variable '{varname}' already declared.\n"
                    f"{stripped}\n        ^\n"
                    f"(original) {original_line.strip()} <-"
                )
            elif not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", varname):
                errors.append(f"Line {idx}: Illegal variable name '{varname}'. \n {stripped} \n         ^")
            else:
                declared_vars[varname] = stripped

        # Handle output
        elif stripped.startswith("output "):
            expr = stripped[7:-1].strip()  # remove 'output ' and trailing ';'
            if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", expr):
                if expr not in declared_vars:
                    errors.append(f"Line {idx}: Output of undeclared variable '{expr}'. \n {stripped} <-")

        # Handle unknown keywords
        elif not any(stripped.startswith(k) for k in ["declare", "output"]):
            keyword = stripped.split()[0]
            errors.append(f"Line {idx}: Unknown keyword '{keyword}'. \n {stripped} \n   ^")

    return errors

# test usage
test_code = """
declare x  5;
"""
'''
for error in run_inspect(test_code):
    print(f"\033[95m{error}\033[0m")
'''

file = sys.argv[1]


with open(file, "r") as f:
    lines = f.readlines()
    code = ""
    index = 0

    while index < len(lines):
        code += lines[index]
        index += 1
    
    possible = run_inspect(code)

    if len(possible) == 0:
        print("[inSPECT BETA] No errors detected")
        subprocess.run(["python3", boot_file, file], check=True)
    else:
        print("[inSPECT BETA] Errors found")
        for error in possible:
            print(f"\033[95m{error}\033[0m")