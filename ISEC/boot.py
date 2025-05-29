import sys
import time
import subprocess
import os
import json

class FileError(Exception):
    pass

#region Important stuff and paths
main_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
isec_path = os.path.join("ISEC", "ast.json")

sys.path.append(main_path)

args = sys.argv
file = args[1]
abs_file = sys.argv[1]
#endregion

with open(file, "r") as f:
    lines = f.readlines()

    i = 0
    depth = 0
    while i < len(lines):
        line = lines[i].strip()

        if lines[0].strip() == "@RawAST":
            i += 1

            ast = []
            while i < len(lines):
                raw = lines[i].strip()
                if raw.count("//"):
                    raw = raw.split("//")[0].strip()
                
                depth += raw.count("[")
                depth -= raw.count("]")

                ast.append(raw)

                if depth == 0 and raw == "]":
                    break

                i += 1

            ast_clean = [line for line in ast if line.strip()]

            raw_json_str = "\n".join(ast_clean)

            try:
                patched = []
                data = json.loads(raw_json_str)

                for node in data:
                    patched.append(node)
                    if node.get("semicolon") != True:
                        patched.append({
                            "semicolon": ";"
                        })

                print(patched)

                with open(isec_path, "w") as ast_file:
                    json.dump(patched, ast_file, indent=2)
            except json.decoder.JSONDecodeError:
                print("Could not decode")
            
            print("[ISEC] Running interpreter based on RawAST...")
            time.sleep(1)
            print("------ OUTPUT ------")
            try:
                subprocess.run(["python3", "ISEC/interpreter.py"], check=True)
            except subprocess.CalledProcessError:
                pass
        i += 1

    if lines[0].strip().count("@") != True:
        print("[ISEC] No special conditions found..")
        time.sleep(.5)

        print("[ISEC] Sending to standard ISEC...")
        time.sleep(.5)
        print("[ISEC] Creating tokens...")
        time.sleep(1)
        subprocess.run(["python3", "ISEC/lexer.py", abs_file], check=True)

        print("[ISEC] Made tokens, now parsing...")
        time.sleep(1)
        subprocess.run(["python3", "ISEC/parser.py"], check=True)

        print("[ISEC] Interpretering...")
        time.sleep(1)
        print("------ OUTPUT ------")
        try:
            subprocess.run(["python3", "ISEC/interpreter.py"], check=True)
        except subprocess.CalledProcessError:
            pass
        
            
        
            
