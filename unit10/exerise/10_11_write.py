import json

filename = 'like_num.txt'
num = input("What is your like num? ")


with open(filename,'w') as f:
    json.dump(num, f)

print(f"I remember you like {num}")

