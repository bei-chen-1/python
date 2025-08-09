"""
# 生成url
base_url = "https://movie.douban.com/top250?start={}&filter="
for i in range(10):
    url = base_url.format(i*25)
    print(url)
"""
# 导入lxml
from lxml import etree

#导入   requests
import requests

class Douban:
    base_url = "https://movie.douban.com/top250?start={}&filter="

    # 定义一个属性用于保存所有url
    def __init__(self):
        self.url_list = []

       #生成所有页面的url地址保存到url_list属性中
        for i in range(10):
            url = self.base_url.format(i * 25)
            self.url_list.append(url)

    #抓取单页数据
    def get_page_data(self,url):
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

    def run(self):
        for url in self.url_list:
            print("-----------------开始抓取页面:",url)
            self.get_page_data(url)
if __name__ == '__main__':
    db = Douban()
    db.run()