#导入   requests
import requests

# 指定图片url
url = "https://www.jd.com/"

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Cookie':'__jda=76161171.1735361484371839777607.1735361484.1735361484.1735361484.1; __jdb=76161171.1.1735361484371839777607|1.1735361484; __jdc=76161171; __jdv=76161171|direct|-|none|-|1735361484373; __jdu=1735361484371839777607; 3AB9D23F7A4B3CSS=jdd03C3VEHZ72H6C56IWEYA2TKZZC3LWAAQNNYI4K4JI3YAGPBX4DDLUZO6UBELBOLAL43ZZOWJW245QVLGESZXC6ZQQDQYAAAAMUBONOQTQAAAAADO6TSTULNVOTAEX; 3AB9D23F7A4B3C9B=C3VEHZ72H6C56IWEYA2TKZZC3LWAAQNNYI4K4JI3YAGPBX4DDLUZO6UBELBOLAL43ZZOWJW245QVLGESZXC6ZQQDQY; _gia_d=1; o2State={%22webp%22:true%2C%22avif%22:true}; areaId=5; ipLoc-djd=5-199-0-0; PCSYCityID=CN_130000_130600_0; shshshfpa=fe341c38-65df-bdcf-378a-46923710b7a8-1735361492; shshshfpx=fe341c38-65df-bdcf-378a-46923710b7a8-1735361492; shshshfpb=BApXSOI6TCPFAwrIol5hTe4VDL-WM1gZyBnd3E71o9xJ1MmG4coG2',
    'Referer':'https://www.jd.com/',
}

# 发送请求requests.get(url=url)获取相应信息(response)
response = requests.get(url=url,headers=headers)

# 写入文件
with open ("jd.html", "w", encoding='utf-8') as f:
    f.write(response.content.decode())