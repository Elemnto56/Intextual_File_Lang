import sys
import os
import subprocess
import json

ask = input("What file to run? (You do not need to include .mtx)\n")

script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, f"{ask}.mtx")
macropath = os.path.join(script_dir, "macros.json")
parserpath = os.path.join(script_dir, "macro_parser.py")

subprocess.run(["python3", parserpath, f"{ask}.mtx"], check=True)

with open(macropath, "r") as f:
    macs = json.load(f)

    for node in macs:
        with open(node["file"], "w") as f:
            for statement in node["code"]:
                f.write(f"{statement}\n")