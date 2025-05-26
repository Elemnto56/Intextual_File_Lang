import subprocess
import time
import os


user = input("What file to run? (You don't need to incude the .itx)\n")
noask = user

with open(f"{noask}.itx", "r") as f:
    source_lines = f.readlines()
    
root = os.path.dirname(os.path.abspath(__file__))
intext_file = os.path.join(root, f"{noask}.itx")
boot_file = os.path.join(root, "ISEC", "boot.py")

print("[ISEC] Checking special conditions...")
time.sleep(1)
subprocess.run(["python3", boot_file, intext_file], check=True)