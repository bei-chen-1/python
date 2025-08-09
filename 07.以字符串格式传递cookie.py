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

# ---------方式二：以字符串格式传递cookie-----------
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    'Referer': "https://passport.china.com/logon",
    'Cookie':'SESSION_COOKIE=46; Hm_lvt_cbec92dec763e6774898d6d85460f707=1716272312; JSESSIONID=E8C2935D3D9A62C369520B06B8FAFAC1; Hm_lpvt_cbec92dec763e6774898d6d85460f707=1716278459; nickname=china_2823hxfg16791058; lastlogindate=2024-05-21; lastlogintime="16:02:24"; lastloginip=183.197.61.99; bindMobile="1@177*****925"; CHINACOMID=11aebc10-cb6e-476d-8072-f953d8bf65a27; CP_USER=FKBo6w-aaDELXK1EnoT3DPk1faoTCuWOzIpsuaQNIsJWqiRz6o9drrZQMJZRRbngi7eJikd0sv41eZDrzksZGmumfJyC7TEP5dMN41%2F1QIHag0K39t%2FVBxzGqQTN85yGDbzc7Mtf21I3yLFRNUeRkJJphQBjDXyUilJ6T4hZkczaUzzJCsTyVeqCVs1bNEBlVJl21LerScqkV2HierMz-5HYL8DoELcjmlLJ6WjemIAiC44IuLq2ow%3D%3D; CP_USERINFO=4Gkk4uas%2FGU6V4cAn8Kr14YtZHaRsQ3bb0iKxhYvuaLYLT-rPEFbvbaQzjvqSKm2v8Fd1lQ14weg0PM1aAxGqjzFStaNWwdXEhS3Zzs0jusNqPIZSkWIUHBpa7NyrsBUv2O8QVvh3O4yqW9wAjnfpw%3D%3D; china_variable=jpEe7N32pYz8SAjCjL8fnh2eLZiI1D/EC6dYmS6/lLUOPrHJGj-IxLIHbACvhNcaC9z3Z8pi2hy0JtYoQGGXmsutg32di8lhAZaSKKJ8BFBt-lJZl7B3R-LY1hWhKpza; lastlogindate=2024-05-21; lastlogintime="16:02:24"; lastloginip=183.197.61.99'
}

# 请求需要登录的页面
res2 = requests.get('https://passport.china.com/',headers=headers)
print(res2.content.decode())