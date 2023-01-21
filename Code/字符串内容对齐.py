s = 'hello python'
print(s.center(20, '*'))  # 居中对齐
print(s.ljust(20, '*'))  # 左对齐
print(s.rjust(20, '*'))  # 右对齐
print(s.zfill(20))  # 右对齐，左边用0填充
# 如果设置的宽度小于原字符串，则返回原字符串
