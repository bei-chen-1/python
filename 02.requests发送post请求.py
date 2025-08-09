"""
发送post请求的功能的方法：
     requests。port()
参数传递：
      1.表单传递：form-data
         requests。port(url,data=字典参数)
      2.json参数:
         requests。port(url,json=字典参数)
"""
# 导入requests
import requests

# 案例一：百度翻译手机版发送post请求 传递表单参数
url = "https://fanyi.baidu.com/sug"

# 请求参数(查询参数)
params = {
    "kw":"python3",
}

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}

# 发送请求获取相应信息(response)
response = requests.post(url=url,data=params,headers=headers)
print(response.content.decode())