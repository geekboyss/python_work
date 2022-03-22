people_0 = {
        'first_name': 'Geek',
        'last_name': 'boy',
        'age': 18,
        'city': 'Shanghai'
        }

people_1 = {
        'first_name': 'xiao',
        'last_name': 'hong',
        'age': 34,
        'city': 'Beijing'
        }


peoples = [people_1, people_0]

for people in peoples:
    full_name = people['first_name'] + " " +  people['last_name']
    print("name : " + full_name +"\n\tage : " + str(people['age']) )
