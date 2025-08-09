#导入requests
import  requests

# 指定url
url = ""

# 获取数据
reponse = requests.get(url)

# 获取json数据:使用json方法获取响应内容
result = reponse.json()

# 获取所有的岗位数据
Posts = result['Data']['Posts']

# 遍历所有的岗位数据
for item in Posts:
    print(item)
    