"""
str :字符串数据类型
bytes :bytes类型数据
encode:对字符串进行编码，转换为二进制格式(bytes类型)
decode:对二进制的字符串(bytes类型)转换为字符串类型
"""
#    字符串
s = '你好'

#字符串转换为bytes类型
res = s.encode()
print(res)

#bytes类型的字符串(二进制字符串)
ss = b'\xe4\xbd\xa0\xe5\xa5\xbd'

#将bytes类型转换为字符串类型
res2 = ss.decode()
print(res2)

