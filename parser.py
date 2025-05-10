import sys

args = sys.argv

if len(args) < 2:
    print("Usage: python3 parser.py <filename>")
    sys.exit(1)

# File name <filename>.itx MUST INCLUDE ITX
filename = args[1]

try:
    file = open(filename)
    for line in file:
        input = line.strip()

        #print("DEBUG: " + input)

        if input[:7] == "output ":
            if input[7:].endswith(';') == True:
                if input[7:].count('"') == 2:
                    print(input[7:].replace(';', '').strip('"'))
                else:
                    print("Error: Something is wrong with your quotes brub brub")                
            else:
                print("Error: Missing a semicolon perhaps?")
        elif input[:8] == "declare"
 

except FileNotFoundError:
    print("Error: Intext file not found")