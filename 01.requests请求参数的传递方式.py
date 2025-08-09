"""
方式一：
      直接拼接在url后面
      https://www.baidu.com/s?ie=UTF-8&wd=%E9%95%BF%E5%9F%8E
      https://movie.douban.com/top250?start=0&filter=

"""
# # 导入requests  方式一：直接拼接在url后面
# import requests
#
# # 指定url
# url = "https://www.baidu.com/s?ie=UTF-8&wd=%E9%95%BF%E5%9F%8E"
#
# # 请求头
# headers = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
#        }
#
# #接收返回的结果
# response = requests.get(url=url,headers=headers)
#
# # 显示获取结果
# print(response.content.decode())


# 导入requests  方式二：通过params参数传递
import requests

# 指定url
url = "https://www.baidu.com/s"

# 请求头
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
       }

# 请求参数(查询参数)
params = {
    'ie': "UTF-8",
    'wd': "长城"
}

#接受返回结果时，使用params进行传递
response = requests.get(url=url,headers=headers,params=params)

# 显示获取结果
print(response.content.decode())