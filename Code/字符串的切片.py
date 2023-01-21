# 切片后会产生新的对象
s = 'hello python'
s1 = s[:5]
s2 = s[6:]
s3 = '!'
newstr = s1+s2+s3
print('!'.join([s1, s2]))

