file = open("main.itx")

for line in file:
    input = line.strip()
    if input.startswith("repeat"):
        logic = input[6:input.index('{')].strip()
        print(logic)
        print("Starts with repeat")
        if logic.count("true") == 1:
            print("Saw true")
            if input.startswith('}'):
                closing_repeat = input
                for thing in input[input.index('{')+1:closing_repeat]:
                    raw_lines = []
                    raw_lines.append(thing)
                    print(raw_lines)