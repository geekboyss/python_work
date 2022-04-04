import json

filename = "like_num.txt"

with open(filename, encoding='utf-8') as f:
    num = json.load(f)
    print(f"I know your favorite number! It's {num}")
