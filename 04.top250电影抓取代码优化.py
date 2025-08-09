"""
# 获取单页数据：

# 导入lxml
from lxml import etree

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

# 读取html网页内容(请求得到的response.content.decode())   ,读取模式     直接读出
page = response.content.decode()

#将获取的网页内容转换为xml
html = etree.HTML(page)

# 定位包含所有数据的元素<ol>再从中找到包含单条数据所有内容的标签<li>
data_list = html.xpath('//ol/li')

# 对定位包含所有元素的列表进行遍历，得到包含单条数据的元素
for li in data_list:
    title = li.xpath(".//span[@class='title'][1]/text()")
    score = li.xpath(".//span[@class='rating_num'][1]/text()")
    number = li.xpath(".//div[@class='star']/span[last()]/text()")
    print("电影的名称:",title[0],"电影的评分:",score[0],"评价人数:",number[0])
"""

"""
准备好top250电影的url,放入列表中
遍历列表中的url，进行抓取
代码优化
"""
# 导入lxml
from lxml import etree

#导入   requests
import requests

def get_data(url):
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    }

    # 发送请求requests.get(url=url)获取相应信息(response)
    response = requests.get(url=url, headers=headers)

    # 读取html网页内容(请求得到的response.content.decode())   ,读取模式     直接读出
    page = response.content.decode()

    # 将获取的网页内容转换为xml
    html = etree.HTML(page)

    # 定位包含所有数据的元素<ol>再从中找到包含单条数据所有内容的标签<li>
    data_list = html.xpath('//ol/li')

    # 对定位包含所有元素的列表进行遍历，得到包含单条数据的元素
    for li in data_list:
        title = li.xpath(".//span[@class='title'][1]/text()")
        score = li.xpath(".//span[@class='rating_num'][1]/text()")
        number = li.xpath(".//div[@class='star']/span[last()]/text()")
        print("电影的名称:", title[0], "电影的评分:", score[0], "评价人数:", number[0])
if __name__ == '__main__':
    get_data("https://movie.douban.com/top250")
    get_data("https://movie.douban.com/top250?start=25&filter=")
    get_data("https://movie.douban.com/top250?start=50&filter=")
    get_data("https://movie.douban.com/top250?start=100&filter=")
    get_data("https://movie.douban.com/top250?start=125&filter=")