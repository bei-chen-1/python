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
print(response.text)