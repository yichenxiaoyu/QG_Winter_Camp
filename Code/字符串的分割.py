s = "hello world"
# 从左侧开始劈分
lis = s.split()  # 默认是空格劈分
print(lis)
s1 = 'hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))

# 从右侧开始劈分
lis = s.split()  # 默认是空格劈分
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))
