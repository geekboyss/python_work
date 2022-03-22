alien_0 = {'x_postion': 0, 'y_postion': 25, 'speed': 'medium'}
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_postion'] = alien_0['x_postion'] + x_increment

print("New x_postion : " + str(alien_0['x_postion']))


