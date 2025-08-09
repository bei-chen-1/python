"""
按照爬虫基本流程
一.数据来源分析
1.明确需求
网址:https://www.douyin.com/user/MS4wLjABAAAAJKyZJ-6arFRSTrGVC8LrJgnY-CwjD0jDgt05BackX8k
数据:视频ID 2.抓包分析
打开开发者工具/刷新网页/关键字搜索找到对应数据
视频工D数据包地址:https://www.douyin.com/aweme/v1/web/aweme/post/

二.代码实现步骤
1.发送请求
模拟浏览器对于url地址发送请求
模拟浏览器：使用请求头中(request headers)的参数内容Cookie/Referer/User-Agent
2.获取数据
获取服务器返回响应数据
3.解析数据
提取我们需要的数据内容:视频链接/视频标题
4.保存数据
获取视频内容，保存本地文件夹
"""

# 导入数据请求模块
import requests

# 导入正则表达式
import re

# 导入解码方法
from urllib.parse import unquote

# 导入json模块
import json

# 导入格式化输出弄块
from pprint import pprint

# 导入自动化模块
from DrissionPage import ChromiumPage

# 打开浏览器
dp = ChromiumPage()

# 监听数据包
dp.listen.start('aweme/post/')

# 访问网站
dp.get('https://www.douyin.com/user/MS4wLjABAAAAJKyZJ-6arFRSTrGVC8LrJgnY-CwjD0jDgt05BackX8k')

for page in range(1,21):
    print(f'正在采集第{page}页的数据')

    # 等待数据包加载
    resp = dp.listen.wait()

    # 获取响应内容
    dp_json = resp.response.body

    # 获取视频ID
    for index in dp_json['aweme_list']:

        # 提取视频ID
        video_id = index['aweme_id']

        # 提取标题
        title = index['desc']

        print(video_id,title)

        """发送请求"""
        # 模拟浏览器
        headers = {
            # Cookie 用户信息,常用于检测是否有登陆账号
            'Cookie':'douyin.com; __ac_referer=__ac_blank; __ac_signature=_02B4Z6wo00f01bufEewAAIDC87mLhdsZMMm7vxVAAAmN5d; ttwid=1%7Ckii33mqBzZD9fDa6Vp4KX5-tNYODRqlsaGnV1LB26X4%7C1735111881%7Cda024f59d5b9bbebd9e039480a5c971714dbd417da8887bbe8ca5ac2ed518579; UIFID_TEMP=3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c215847763c61e9f3281ba6ba6c31584a0d03eefbabb8118ba060bc66db09b7c80ac212253ad875ef397a9ab9fd250cafe; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; architecture=amd64; dy_swidth=1366; dy_sheight=768; csrf_session_id=853c070b7f10cb2d5408c06c69fdce95; strategyABtestKey=%221735111887.038%22; is_dash_user=0; fpk1=U2FsdGVkX187GFQvwNzQ1qaoYGzgvvHbfpiUoNHFq32gEEpp3szfg8d9d8c6STU+cCRbGIuVUEZqNhHKgaXSTw==; fpk2=f1f6b29a6cc1f79a0fea05b885aa33d0; s_v_web_id=verify_m53ktil2_MFsTzg51_YukK_4vnF_AnMa_75keX9xRwyQ4; xgplayer_user_id=985000766054; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; passport_csrf_token=b8e3d06cf57389d42b3d96cfab53276c; passport_csrf_token_default=b8e3d06cf57389d42b3d96cfab53276c; xg_device_score=6.09; biz_trace_id=4e348a64; bd_ticket_guard_client_web_domain=2; passport_assist_user=CkHP76ndhkWxhkMgsVTP2NHs12MJeZscFnzVK4suZw65xK5byfbEsgAy5KkhQtY2aGbp1OfVbFguwotG0uFJWQWgnhpKCjzypclh-74pdbkgRWFHe4pZhuFoO570ZT5kWm7xBnX1AtXOoC_6HkxtvYfNL2TIF4wAJ8Insk_ubyt6CZsQ-oXlDRiJr9ZUIAEiAQOEZIUo; n_mh=YN0lW_piMoOC8jpYqk6ixMFlLNLLSdXnnWvd15hviuw; sso_uid_tt=631545c1bef8f37af816aaf5acdc024a; sso_uid_tt_ss=631545c1bef8f37af816aaf5acdc024a; toutiao_sso_user=a406a1565d2cfc592a75386be08a64ea; toutiao_sso_user_ss=a406a1565d2cfc592a75386be08a64ea; sid_ucp_sso_v1=1.0.0-KDE5OWEyN2NkNGQyZWIyMzViMjEwMDQ1ZjM1MjNjMjM1NDBhYTIzZWQKIQjb69H4g8ydAxDr6a67BhjvMSAMMLvkj7AGOAZA9AdIBhoCbGYiIGE0MDZhMTU2NWQyY2ZjNTkyYTc1Mzg2YmUwOGE2NGVh; ssid_ucp_sso_v1=1.0.0-KDE5OWEyN2NkNGQyZWIyMzViMjEwMDQ1ZjM1MjNjMjM1NDBhYTIzZWQKIQjb69H4g8ydAxDr6a67BhjvMSAMMLvkj7AGOAZA9AdIBhoCbGYiIGE0MDZhMTU2NWQyY2ZjNTkyYTc1Mzg2YmUwOGE2NGVh; login_time=1735111913753; passport_auth_status=09dc40c4838c4269f020618789415cb0%2C; passport_auth_status_ss=09dc40c4838c4269f020618789415cb0%2C; uid_tt=2ecbeceff2ad0b726d34b5e859ff9f3c; uid_tt_ss=2ecbeceff2ad0b726d34b5e859ff9f3c; sid_tt=db3707d104b7656812e4fadb01a55b8b; sessionid=db3707d104b7656812e4fadb01a55b8b; sessionid_ss=db3707d104b7656812e4fadb01a55b8b; is_staff_user=false; UIFID=3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c24880bba84d218682656f134413f22a6997aba1b196850693d8f94871c8fc5492fccd3a04edaff0eac191dd77982553a52549f1d8e5428682aa574defe415573a9a33c38de0926a3aeac7b33f9324bda8bb10f9b92aeed9d841c55b7e31b8558f1fd47528b04739fa285042e6ac6b9ceb77f21896d32ef296f0cdd9285d56bc37; publish_badge_show_info=%220%2C0%2C0%2C1735111916425%22; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=2cd7c0c59e1d4fa45edad137317f95e8; __security_server_data_status=1; sid_guard=db3707d104b7656812e4fadb01a55b8b%7C1735111925%7C5183993%7CSun%2C+23-Feb-2025+07%3A31%3A58+GMT; sid_ucp_v1=1.0.0-KGU0MzRiYjI5ZDFmNWY0Y2E2ZDljNTc2M2QwYTdmYzk4ODIzNGY3ZTEKGwjb69H4g8ydAxD16a67BhjvMSAMOAZA9AdIBBoCaGwiIGRiMzcwN2QxMDRiNzY1NjgxMmU0ZmFkYjAxYTU1Yjhi; ssid_ucp_v1=1.0.0-KGU0MzRiYjI5ZDFmNWY0Y2E2ZDljNTc2M2QwYTdmYzk4ODIzNGY3ZTEKGwjb69H4g8ydAxD16a67BhjvMSAMOAZA9AdIBBoCaGwiIGRiMzcwN2QxMDRiNzY1NjgxMmU0ZmFkYjAxYTU1Yjhi; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; __ac_nonce=0676bbd4700903db458bc; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1366%2C%5C%22screen_height%5C%22%3A768%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A9.35%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRU5SMEljbHhxcGtoRlNnbVNqMnVmdTZ1NmRYR25LaDJmL0paZGxZM0d1Z0JjeG5iQmFxa1RKZWlNYXE0L0J0ZWtlUHVPZ2dwQTc1emxLd0MrMnR6TG89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; odin_tt=2a8ad55792a5fdf5760a927c8a5aafe91f76ef8e49d9ec4e1ff0fdd8ad472014cabd4edc1577ab4f6e9d9d51a3523031; download_guide=%223%2F20241225%2F0%22; IsDouyinActive=false; passport_fe_beating_status=false',
            # Referer 防盗链，告诉服务器请求网址从哪里跳转过来的
            'Referer':'https://www.douyin.com/user/MS4wLjABAAAAJKyZJ-6arFRSTrGVC8LrJgnY-CwjD0jDgt05BackX8k',
            # User-Agent 用户代理，表示浏览器、设备基本身份信息
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

        # 请求网址
        url = f'https://www.douyin.com/user/MS4wLjABAAAAJKyZJ-6arFRSTrGVC8LrJgnY-CwjD0jDgt05BackX8k?from_tab_name=main&modal_id={video_id}'

        # 发送请求
        response = requests.get(url=url,headers=headers)


        """获取数据"""
        # 获取相应的文本信息
        html = response.text


        """解析数据"""
        # 提取视频信息
        info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>', html)[0]

        # 解码数据
        json_str = unquote(info)

        # 把json字符串转成json字典数据 pprint(json_data)
        json_data =  json.loads(json_str)

        # 提取视频链接
        video_url = 'https:' + json_data['app']['videoDetail']['video']['bitRateList'][0]['playAddr'][0]['src']

        # 清除文件名中的非法字符
        illegal_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '\n']


        def clean_filename(title):
            for char in illegal_chars:
                title = title.replace(char, "")
            return title

        # 提取视频标题
        title = json_data['app']['videoDetail']['desc']
        # print(video_url)
        print(clean_filename(title))

        """保存数据"""
        # 获取视频内容
        video_content = requests.get(url=video_url, headers=headers).content

        # 数据保存
        with open('video\\' + clean_filename(title) + '.mp3', mode='wb') as f:
            # 写入数据内容
            f.write(video_content)

    dp.scroll.to_bottom()