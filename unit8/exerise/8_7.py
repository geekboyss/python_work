def make_album(name, album, num = ''):
    album = {name : album,}
    if num:
        album['num'] = num
    return album


result = make_album('zhangjie', 'kuangye')
print(result)

result = make_album('zhangze', 'yema', num = 10)
print(result)

