# 将字符串转换成二进制数据
s = '天涯共此时'
print(s.encode(encoding='GBK'))  # 在GBK，一个中文占两个
print(s.encode(encoding='UTF-8'))  # 在UTF-8，一个中文占三个


# 将二进制数据转换成字符串
byte = '天涯共此时'.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))  # 解码

byte = '天涯共此时'.encode(encoding='uTF-8')
print(byte.decode(encoding='UTF-8'))  # 解码


