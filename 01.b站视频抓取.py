"""
视频url:
音频url：
"""
# 导入requests
import requests

# 请求头
headers = {
    'User-Agent': "",
    'Cookie': "",
    'Referer':""
}

# 视频url
url1 = ""

# 音频url
url2 = ""

# 发起请求
resp1 = requests.get(url1, headers=headers)
resp2 = requests.get(url2, headers=headers)

with open('sp1.mp4', 'wb') as f:
    f.write(resp1.content)
with open('sp2.mp4', 'wb') as f:
    f.write(resp2.content)

"""
开始视频合成
安装MoviePy   pip install MoviePy
"""
# 开始视频合成
from moviepy.editor import ffmpeg_tools

# 将本地的hh2.MP4和hh3.MP4 合成为 下载文件.MP4
ffmpeg_tools.ffmpeg_merge_video_audio('sp1.np4','sp2.mp4','下载视频.mp4')