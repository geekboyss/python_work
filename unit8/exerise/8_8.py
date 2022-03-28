def make_album(name, album, num = ''):
    album = {name : album,}
    if num:
        album['num'] = num
    return album


while True:
    n = input("Enter name: ")
    if n == 'q':
        break
    a = input("Enter album: ")
    if n == 'q':
        break
    result = make_album(n, a)
    print(result)


