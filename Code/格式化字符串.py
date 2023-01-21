name = '张三'
age = 18
print('我叫%s，今年%d岁' % (name, age))

print('{0},{1}'.format(name, age))

print(f"{name},{age}")

print('%10d' % 99)  # 宽度
print('%.3f' % 3.14159)  # .3表示小数点后三位
print('%10.3f' % 3.14159)  # 宽度10，保留雄安舒后三位

print('0:10.3'.format(3.14159))  # 0是索引 10是宽度 .3保留三位有效数字

