# 导入requests
import requests

# 导入time
import time

# 写入文件
f = open ("岗位.txt",'a',encoding='utf-8')

# 设置抓取页数
for i in range(1,11):

    # 指定url
    url = "https://careers.tencent.com/tencentcareer/api/post/Query"

    # 请求参数(查询参数)
    params = {
        'pageIndex':i,
        'timestamp':int(time.time()*100),
        'categoryId':"40008,40002001,40002002,40003001,40003002,40003003,40004,40005001,40005002,40006,40007,40009,40010,40011,40001001,40001002,40001003,40001004,40001005,40001006",
        'attrId':"1,3,2,5",
        'pageSize':20,
        'language':"zn-cn",
        'area':"cn",
        'countryId':"",
        'cityId':"",
        'bgIds':"",
        'productId':"",
        'keyword':"",
    }

    # 获取数据
    reponse = requests.get(url,params)

    # 获取json数据:使用json方法获取响应内容
    result = reponse.json()

    # 获取所有的岗位数据
    Posts = result['Data']

    # 遍历所有的岗位数据
    for item in Posts:
        print(item)
        # 将岗位写入文件
        # f.write(str(item))

# 关闭文件
f.close()