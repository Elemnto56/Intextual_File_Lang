import subprocess
import time
import os

user = input("What file to run? (You don't need to incude the .itx)\n")

root = os.path.dirname(os.path.abspath(__file__))
intext_file = os.path.join(root, f"{user}.itx")
lexer_file = os.path.join(root, "ISEC", "lexer.py")
parser_file = os.path.join(root, "ISEC", "parser.py")
interpreter_file = os.path.join(root, "ISEC", "interpreter.py")

print("[ISEC] Lexing Intext code...")
time.sleep(1)
subprocess.run(["python3", lexer_file, intext_file], check=True)

print("[ISEC] Parsing tokens...")
time.sleep(1)
subprocess.run(["python3", parser_file], check=True)

print("[ISEC] Interpreting AST...")
time.sleep(1)
print("-------- OUTPUT --------")
subprocess.run(["python3", interpreter_file], check=True)