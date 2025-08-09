"""
发送post请求的功能的方法：
     requests。port()
参数传递：
      1.表单传递：form-data
         requests。port(url,data=字典参数)
      2.json参数:
         requests。port(url,json=字典参数)
      3.参数：
        code: ""
        email: "3435539036@qq.com"
        encryption: 1
        mobile: ""
        password: "JFA1SybtPsT1KiKg3ZinYA=="
        remember: "0"
        reqtimestamp: 1716270537480
        type: "login"
"""
# 导入requests
import requests

# 案例二：课堂派发送POST请求  传递json参数
url = "https://openapiv5.ketangpai.com//UserAPI/login"

# 请求参数(查询参数)
params = {
    'code':"",
    'type':"login",
    'reqtimestamp': 1716270537480,
    'remember': "0",
    'password': "JFA1SybtPsT1KiKg3ZinYA==",
    'email': "3435539036@qq.com",
    'mobile': ""
}

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}

# 发送请求获取相应信息(response)
response = requests.post(url=url,json=params,headers=headers)
# print(response.content.decode())
# print(response.json())