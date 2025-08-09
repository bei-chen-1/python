#导入   requests
import requests
# 导入time
import  time
# 导入lxml
from lxml import etree
def get_edu_name():
    # for循环
    for i in range(1,242):
        # 定义url
        url = "https://src.sjtu.edu.cn/rank/firm/0/?page="+str(i)
        # 请求头
        headers = {
             "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
        }
        # 发送请求requests.get(url=url)获取相应信息(response)
        result = requests.get(url,headers=headers).content.decode('utf-8')
        # 将获取的网页内容转换为HTML
        aa = etree.HTML(result)
        # 筛选内容
        name = aa.xpath('//td[@class="am-text-center"]/a/text()')
        print('第' + str(i)+'页')
        print(name)
        name = '\n'.join(name)
        with open('edu_name.txt','a+') as f:
            f.write(name+'\n')
            f.close()
        time.sleep(1)
if __name__ == '__main__':
    # 使用函数
    get_edu_name()