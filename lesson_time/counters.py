def count_letters(input_string):
    result = {}    
    for c in input_string:
        result[c] = input_string.count(c)
    return result

def count_letters2(input_string):
    result = {}
    for c in input_string:
        result[c] = result.get(c, 0) + 1 
    return result 

def print_dict(d):
    for key, value in d.items():
        print(f"{key}: {value}")

print(__name__)
if __name__ == "__main__":
    result1 = count_letters("Hello, PyLadies!")
    result2 = count_letters2("Hello, PyLadies!")

    print_dict(result1)
    print()
    print_dict(result2)

