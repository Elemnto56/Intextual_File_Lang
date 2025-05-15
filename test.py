def read(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error: Couldn't read file '{path}'")
        return None
    
print(read("text.txt"))