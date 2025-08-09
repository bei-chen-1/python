#导入   requests
import requests

# 指定图片url
url = "https://gips0.baidu.com/it/u=2298867753,3464105574&fm=3028&app=3028&f=JPEG&fmt=auto?w=960&h=1280"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}

# 发送请求requests.get(url=url)获取相应信息(response)
response = requests.get(url=url,headers=headers)

'''
将响应的内容写入到一个图片文件中

 写     打开      文件名.类型 ，   打开模式wb二进制      没有此文件则新建一个
with   open    ("小老虎.jpg" ,      "wb"      )     as f:
              写    响应  .  响应内容
         f.write(response.content)
'''
with open ("小老虎.jpg", "wb") as f:
    f.write(response.content)