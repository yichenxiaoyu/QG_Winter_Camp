s = 'hello,hello'
print(s.index('lo'))   # 3 从左边开始寻找
print(s.find('lo'))    # 3 如果没有不会报错，会返回-1
print(s.rindex('lo'))  # 9 r是从右边开始寻找
print(s.rfind('lo'))   # 9 如果没有不会报错，会返回-1

print(s.index('p'))    # ValueError
print(s.find('p'))     # -1
print(s.rindex('p'))   # ValueError
print(s.rfind('p'))    # -1
