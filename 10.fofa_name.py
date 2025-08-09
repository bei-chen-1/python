#导入   requests
import requests
#导入time
import  time
#导入lxml
from lxml import etree
#导入base64
import base64
def search_name(search,shuliang):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer":"https://fofa.info/",
        "Cookie":"_ga=GA1.1.2007290192.1723460591; is_flag_login=0; befor_router=; isRedirectLang=1; is_mobile=pc; Hm_lvt_4a3f4dd5efb420651f5c2d19cd4b1e6b=1723460590,1723462269,1723518588; HMACCOUNT=9D0C8FA0A78807E0; baseShowChange=false; viewOneHundredData=false; __fcd=G25PiKepHDWCmT4kOgnLEfcA; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6Mzk0MTc4LCJtaWQiOjEwMDIyNjU1MCwidXNlcm5hbWUiOiJiZWltaTEwMDkiLCJleHAiOjE3MjM3NzgwNzl9.vT2akjdUVvSoSZnUcywBovrzwD-cVtQieMvPQ3zB5pzV1B0CYR2NZSC3f9yRYNwz1FiZVbtCTJUBJ51kdyDJ-g; user=%7B%22id%22%3A394178%2C%22mid%22%3A100226550%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22beimi1009%22%2C%22nickname%22%3A%22beimi1009%22%2C%22email%22%3A%223435539036%40qq.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22key%22%3A%2271c8e4091cf952f857d881d25b61388f%22%2C%22category%22%3A%22user%22%2C%22rank_avatar%22%3A%22%22%2C%22rank_level%22%3A0%2C%22rank_name%22%3A%22Registered%20User%22%2C%22company_name%22%3A%22beimi1009%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22fofa_point%22%3A0%2C%22credits%22%3A1%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%2C%22data_limit%22%3A%7B%22web_query%22%3A300%2C%22web_data%22%3A3000%2C%22api_query%22%3A0%2C%22api_data%22%3A0%2C%22data%22%3A-1%2C%22query%22%3A-1%7D%2C%22expiration_notice%22%3Afalse%2C%22remain_giveaway%22%3A0%2C%22fpoint_upgrade%22%3Afalse%7D; Hm_lpvt_4a3f4dd5efb420651f5c2d19cd4b1e6b=1723518907;"
    }
    proxys = {
        'http':'http://127.0.0.1:51427',
        'https':'https://127.0.0.1:51427'
    }
    base_search = str(base64.b64encode(search.encode("utf-8")),"utf-8")
    for i in range(1,shuliang+1):
        url = 'https://fofa.info/result?qbase64='+ base_search +'&page='+str(i)+'&page_size=10'
        res = requests.get(url,headers=headers,proxies=proxys).content
        aa = etree.HTML(res)
        ip = aa.xpath('//a[@target="_blank"]/@href')
        print('第'+str(i)+'页：')
        print(ip)
        ip = '\n'.join(ip)
        with open('fofa_name.txt', 'a+') as f:
            f.write(ip + '\n')
            f.close()
        time.sleep(1)
if __name__=='__main__':
    search_name('"title="上海交通大学" && country="CN""',1)
    #search_name('"edu.cn" && "country+""CN" && ""ManageEngine"', 要爬几页)