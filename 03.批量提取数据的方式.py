"""
导入lxml
将获取的网页内容转换为xml
通过xpath去定位和解析页面中的内容

xpath数据提取技巧：
    1.定位包含所有数据的元素<ol>    //ol
    2.再从中找到包含单条数据所有内容的标签<li>    //ol/li
    3.对定位包含所有元素的列表进行遍历，得到包含单条数据的元素
    4.在提取单条数据中的详细内容
"""
# 导入lxml
from lxml import etree

# 读取html网页内容(请求得到的response.content.decode())   ,读取模式     直接读出
page = open('douban.html', 'r', encoding='utf-8').read()

#将获取的网页内容转换为xml
html = etree.HTML(page)

# 定位包含所有数据的元素<ol>再从中找到包含单条数据所有内容的标签<li>
data_list = html.xpath('//ol/li')

# 显示li标签
# print(data_list)

# 对定位包含所有元素的列表进行遍历，得到包含单条数据的元素
for li in data_list:
    title = li.xpath(".//span[@class='title'][1]/text()")
    score = li.xpath(".//span[@class='rating_num'][1]/text()")
    number = li.xpath(".//div[@class='star']/span[last()]/text()")
    print("电影的名称:",title[0],"电影的评分:",score[0],"评价人数:",number[0])