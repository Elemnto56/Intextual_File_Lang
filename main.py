import subprocess
import time
import os
import sys

try:
    special_check = sys.argv[1]
    if special_check == "--nowait":
        given = input("What file to run? (You don't need to incude the .itx)\n")
        subprocess.run(["python3", "ISEC/lexer.py", f"{given}.itx"], check=True)

        subprocess.run(["python3", "ISEC/parser.py"], check=True)

        print("------ OUTPUT ------")
        subprocess.run(["python3", "ISEC/interpreter.py"], check=True)
        sys.exit(0)

    if special_check == "--dev":
        print("!--- Welcome Developer ---!")
        print("""
        1. Macros
        """)
        option = input("> ")
        option = int(option)

        match option:
            case 1:
                os.execv(sys.executable, [sys.executable, os.path.abspath("ISEC/macro_system/macro_handle.py")])
    
    if special_check == "--version" or special_check == "--v":
        print("""
        +----------------------------------+
        |      Intext Language v0.6.3      |
        |       "Spaghetti & Crunch"       |
        +----------------------------------+

        > Spaghetti Output
        > crunch() support
        > read() support
        > Error-handling enhancements

        Built by: Elemnto56
        """)
        sys.exit(0)
    
                
except IndexError:
    pass


user = input("What file to run? (You don't need to incude the .itx)\n")
noask = user

with open(f"{noask}.itx", "r") as f:
    source_lines = f.readlines()
    
root = os.path.dirname(os.path.abspath(__file__))
intext_file = os.path.join(root, f"{noask}.itx")
boot_file = os.path.join(root, "ISEC", "boot.py")

try:
    ast_file = os.path.join(root, "ISEC", "ast.json")
    token_file = os.path.join(root, "ISEC", "tokens.json")
    os.remove(ast_file)
    os.remove(token_file)
except FileNotFoundError:
    pass

print("[ISEC] Checking special conditions...")
time.sleep(1)
subprocess.run(["python3", boot_file, intext_file], check=True)
