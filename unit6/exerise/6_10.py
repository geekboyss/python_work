name_num = {
        'Alex': [12, 43, 54],
        'Geek': [43, 3 , 22],
        'Tom': [32, 19, 90],
        }

for name , nums in name_num.items():
    print("name : " + name )
    for num in nums:
        print("\t" + str(num))



