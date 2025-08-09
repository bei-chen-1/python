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

#请求头(字典格式)
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}

#使用requests发送请求：请求百度首页
requests.get(url=url,headers=headers)

#接受返回的结果
response = requests.get(url=url,headers=headers)

#打印结果
print(response.content.decode())

# 获取请求的请求头信息
print(response.request.headers)
"""
{
'User-Agent'(客户端身份): 'python-requests/2.31.0', 
'Accept-Encoding'(解码类型): 'gzip, deflate', 
'Accept'(请求的数据): '*/*', (任何数据)
'Connection'(连接形式): 'keep-alive'(保持长连接)
}
"""