#导入   requests
import requests

# 指定图片url
url = "https://movie.douban.com/top250"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}

# 发送请求requests.get(url=url)获取相应信息(response)
response = requests.get(url=url,headers=headers)

# 写入文件
with open ("douban.html", "w", encoding='utf-8') as f:
    f.write(response.content.decode())