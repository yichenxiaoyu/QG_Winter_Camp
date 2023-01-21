s = 'hello world'
a = s.upper()  # 转换成大小后会产生一个新的字符串
b = s.lower()  # 小写

s2 = 'hello,Python'
c = s2.swapcase()  # HELLO,pYTHON
d = s2.title()  # Hello,Python

print(a, id(a))