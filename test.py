def contains(word, where):
    if word not in where:
        return False
    else:
        return True
    
string = "Hello World"

try:
    print(contains("Hello", string, "something"))
except TypeError:
    print("Too many args")