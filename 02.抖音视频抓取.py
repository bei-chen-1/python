"""
视频
url = https://www.douyin.com/aweme/v1/play/?video_id=v0200fg10000cp6vh3vog65paio4vud0&line=0&file_id=911d2050e09548bcaf042affd992f9ed&sign=9c4d93213847699cc113aa9310f13df4&is_play_url=1&source=PackSourceEnum_FEED&aid=6383
"""
# 导入
import requests

# 指定url
url = "https://www.douyin.com/aweme/v1/play/?video_id=v0200fg10000cp6vh3vog65paio4vud0&line=0&file_id=911d2050e09548bcaf042affd992f9ed&sign=9c4d93213847699cc113aa9310f13df4&is_play_url=1&source=PackSourceEnum_FEED&aid=6383"

# 请求头
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    'Cookie': "",
    'Referer':""
}

# 发起请求
response = requests.get(url=url,headers=headers)

# 写入文件
with open("抖音视频.mp4", 'wb') as f:
    f.write(response.content)

