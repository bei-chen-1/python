"""
准备：安装requests库  pip install requests
     导入requests库  import requests
需求：使用代码获取网站首页内容
步骤：
    1、地址：https://baidu.com/
    2、发送请求：
               requests.get(url='请求地址‘)
    3、获取返回信息：
"""
#导入requests请求魔模块
import requests

#指定地址
url = "https://baidu.com/"

#使用requests发送请求：请求百度首页
requests.get(url=url)

#接受返回的结果
response = requests.get(url=url)

#打印结果
#print(response.text)
# print(response.content.decode())
"""
响应数据的获取:
方式一：response.text           获取的是字符串
方式二：response.content        获取的是原始二进制数据(bytes类型数据)
方式三：response.content.decode()   decode:对二进制的字符串(bytes类型)转换为字符串类型
"""

# 获取http状态码
status = response.status_code

#获取响应对应的请求头
qqt = response.request.headers

#获取响应头
headers = response.headers

#获取cookies
cookies = response.cookies

#获取响应对应的请求cookies
xdq = response.request.cookies