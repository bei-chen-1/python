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

#通过xpath去定位和解析提取页面中的内容
# titles = html.xpath("//*[@class='title']")

# 获取文本
titles = html.xpath("//*[@class='title'][1]/text()")

# 获取评分
score = html.xpath("//*[@class='rating_num'][1]/text()")

# 显示共有多少个
# print(len(titles))

# 显示内容
print(titles)
print(score)