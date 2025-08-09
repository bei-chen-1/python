"""
模拟登录，访问需要登陆之后才能打开的页面
    1.发送登录请求
    2.保存cookie信息
    3.携带cookie信息请求需要登陆的页面
    4.传递cookie方式：
      方式一：以字典格式传递
        cookie = {}
        requests.post(cookie=cookie)
      方式二：以字符串格式传递
        headers = {
        'Cookie':"字符串格式cookie值"
        }
         requests.get()
"""
# 导入requests
import requests

# 登陆地址
login_url = "https://passport.china.com/logon"

# 请求参数(查询参数)
params = {
    'userName':"17775990925",
    'password':"a546245426"
}

# 请求头
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    'Referer': "https://passport.china.com/logon"
}

# 发送请求进行登录(response)
response = requests.post(url=login_url,data=params,headers=headers)
print(response.content.decode())

# ---------方式一：以字典格式传递cookie-----------

# 获取cookie信息
cookie = response.cookies

# 请求需要登录的页面
res2 = requests.get('https://passport.china.com/',headers=headers,cookies=cookie)
print(res2.content.decode())