current_users = ['Alex', 'Bob', 'Anan', 'Geek', 'Tom']

new_users = ['Bob', 'Cat', 'Geek', 'Gdp']

for new_user in new_users:
    if (new_user.title() in current_users):
        print("You need another name")
    else:
        print("This name no use")
