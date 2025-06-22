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

    elif special_check == "--dev":
        print("!--- Welcome Developer ---!")
        print("""
        1. Macros
        """)
        option = input("> ")
        option = int(option)

        match option:
            case 1:
                os.execv(sys.executable, [sys.executable, os.path.abspath("ISEC/macro_system/macro_handle.py")])
    
    elif special_check == "--version" or special_check == "--v":
        print("""
        >>> Intextual File Language 0.7
        >>> Project File Fusion
        >>> Developed by: Elemnto56

        --- Included in this build ---
        ✔ read/write/append/delete file ops
        ✔ <<< Text Bloc >>> multiline support
        ✔ input() with prompt functionality
        ✔ insPECT: pre-runtime error checking
        -------------------------------
        A scripting language designed to scale automation, not complexity.
        """)
        sys.exit(0)
    
    elif special_check == "--help":
        print("""
        Usage:
        python3 main.py [--option]

        Options:
        --help                  Show this help message and exit
        --v or --version        Show version information
        --nowait                Runs ISEC with no wait time at all, along with no logs
        --dev                   Opens Developer Menu
              
        About:
        Intext is a lightweight scripting language focused on
        file automation and a simple output pipeline.

        Created by: Elemnto56
        """)
        sys.exit(0)
    
    else:
        print("The inputted special argument is not valid")
        sys.exit(1)
    
                
except IndexError:
    pass


user = input("What file to run? (You don't need to incude the .itx)\n")
noask = user

with open(f"{noask}.itx", "r") as f:
    source_lines = f.readlines()
    
root = os.path.dirname(os.path.abspath(__file__))
intext_file = os.path.join(root, f"{noask}.itx")
boot_file = os.path.join(root, "ISEC", "boot.py")
inspect = os.path.join(root, "inSPECT.py")

try:
    ast_file = os.path.join(root, "ISEC", "ast.json")
    token_file = os.path.join(root, "ISEC", "tokens.json")
    os.remove(ast_file)
    os.remove(token_file)
except FileNotFoundError:
    pass

print("[ISEC] Sending to bootloader...")
time.sleep(1)
subprocess.run(["python3", boot_file, intext_file], check=True)
