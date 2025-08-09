
#导入   requests
import requests

# 指定歌曲url
url = "https://m801.music.126.net/20240518151902/76009f53fc78d5fb0bcd97232dac745f/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/36033303850/01e3/e373/23d3/4fc9b631eecdf5079be76c28e853985b.m4a"

# 请求头
headers = {
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}

# 发送请求requests.get(url=url)获取相应信息(response)
response = requests.get(url=url)

# 写入文件(视频，图片，音频都需要用wb模式)
with open ("红草莓.m4a", "wb") as f:
    f.write(response.content)