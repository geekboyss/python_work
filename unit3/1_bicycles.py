from email import message


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
# print(bicycles[0].title())
print(bicycles[-1])

# 3.1.3
print('----------')
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)