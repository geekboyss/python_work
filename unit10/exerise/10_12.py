import json

def get_stored_num():
    filename = 'like_num.json'
    try:
        with open(filename) as f:
            num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return num

def get_new_num():
    num = input("What is you like num ")
    filename = 'like_num.json'
    with open(filename, 'w') as f:
        json.dump(num, f)
    return num

def greet_user():
    num = get_stored_num()
    if num:
        print(f"I know your favorite number! It's {num}")
    else:
        num = get_new_num()
        print(f"I remember you like {num}")

greet_user()
