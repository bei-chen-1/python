"""
按照爬虫基本流程
一.数据来源分析
1.明确需求
网址:https://www.douyin.com/user/MS4wLjABAAAArcoz8pyUJSASISQnP_JMfUgNATaCTOJJzQsG6HSzeAU
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
dp.get('https://www.douyin.com/user/MS4wLjABAAAArcoz8pyUJSASISQnP_JMfUgNATaCTOJJzQsG6HSzeAU')

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
            'Cookie': 'douyin.com; __ac_nonce=0676b9c500067e030b440; __ac_signature=_02B4Z6wo00f01cS8tqAAAIDCjJosy-taJ43EnLIAABZG51; ttwid=1%7CRpPtQCn5sbaFpyAGMKc7f5CPB8xRAB57fdaeANAhCkQ%7C1735105617%7C47c5fa0daf088fc40fe152d807d896e91e4e1f6b796e6f268b64988dc3893785; UIFID_TEMP=3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c215847763c61e9f3281ba6ba6c31584a031cd880365ac1c20ac2acc94b2dcd1beadce009f55588f311be2494f0c778f39; s_v_web_id=verify_m53h32ob_Rl2AOi2O_G57L_4YPX_9fk8_EqiCFGFnhJkh; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; architecture=amd64; dy_swidth=1366; dy_sheight=768; csrf_session_id=853c070b7f10cb2d5408c06c69fdce95; strategyABtestKey=%221735105621.148%22; is_dash_user=0; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; xgplayer_user_id=936747542235; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; fpk1=U2FsdGVkX1+QUJf/rGibwKOpAAZv/oA11EReKyTjIGxxE6/lcXLqGFr+sJwa+15TqrAVxL/svJ1DFb0g6Iyb1Q==; fpk2=f1f6b29a6cc1f79a0fea05b885aa33d0; passport_csrf_token=eb19b558fc20774dfb9ab7d452e85399; passport_csrf_token_default=eb19b558fc20774dfb9ab7d452e85399; xg_device_score=6.905294117647059; biz_trace_id=4169d9a1; bd_ticket_guard_client_web_domain=2; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e5827292771273f2736363c323733303534303632342778; bit_env=RTaZVuLtRaIQPzTrtEdqMMDunH7hH8_rbbZuxy6yGMfPlL5LfX_6vyTMVr5YpoSIqig3Jj4mvagGXPlME4yDoNGrpof7j48DOGZRp4ziQG5dg7TyzWKMyUIITfj6EKujOSQMda5VrMrxCOXNMTJ26yQdxYcmNSXburtF2ZkFd7CLJO4FFoPXJfTOFaoDx7su-yn6VeGv2PzlOf_puHzbvMvEApdokR3wEV6_JMA4ztao5cEqrAP2-3XSH5BlWsuVr2gvwTFwOW44rgB7EjKoGRdUUJD2XkIguzCgtZgTkFiw5CTL8-kjLmbzGSs6pewET-b9UMIXmMHbLc6UldFffdOd0UqhJo2N1ZhJrcN2BmTyhThKnMbKwD_xYGFuuaCUF4c7hI3Pgq3t5YPFxUXfCCtG_Yr14tiybeGwIKxl0GMBXgp-Y5kcqlth9WcAVjN_oMAOpKy6yu3xJcFrxjG9eZGmzpDAuhVwcisvbBiW0a1045LThXfGRG0ndagOayG4; gulu_source_res=eyJwX2luIjoiMGQzYzY5YzlkNGIwYzg0ODM5NjlhMDVhZmI1ZmYyNGViYjQ3YTM3MzE4OTY3MDIyZWRmNDc0NWM4MGQ4ODk4NyJ9; passport_auth_mix_state=f7e2dhgapbmqjshxiv93egz86n14rboiamlhhz8h8gt0xd59; UIFID=3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c24880bba84d218682656f134413f22a69a43bfada404371d3b68cd07c6fe50752db3b4497a8e34ddcc49fd6f66a5212d6547e32bedbe20cf419146a21efa9cb415a7fc8ccf3dc9a23f9bb924c2c2480d6ada838285c4322680f7a4ace78a07290f86b429e35ba37498031e687c208d6264c94470be10241266bfdd7763749c6d0; passport_assist_user=CkE5ZngFecmMwCfELt1s8NNCCnz7hl9DdjE9aZQP1YLd3sCsisVFIVIb_XRiMkVQMt2cbLPBbro1BmXn99S7YncQExpKCjzc6BC1RXP6hqYO612UURJUVo92D3gemRyh5oW7iUrCSgYsY9e2efnaq9-yW6Dc0M09zylNX5ZpDdoUwUsQ2ILlDRiJr9ZUIAEiAQPqwssw; n_mh=YN0lW_piMoOC8jpYqk6ixMFlLNLLSdXnnWvd15hviuw; sso_uid_tt=60c48a4bb7a2104f4fc7af64e216e05e; sso_uid_tt_ss=60c48a4bb7a2104f4fc7af64e216e05e; toutiao_sso_user=2463ec031d1b85a80ada691ac60c0bd1; toutiao_sso_user_ss=2463ec031d1b85a80ada691ac60c0bd1; sid_ucp_sso_v1=1.0.0-KGRlYmJhNzU4NzhiODc0MjFkYmRkYWE5MzljNjU4NmI0YjBlNGU4NmMKIQjb69H4g8ydAxCKua67BhjvMSAMMLvkj7AGOAZA9AdIBhoCbGYiIDI0NjNlYzAzMWQxYjg1YTgwYWRhNjkxYWM2MGMwYmQx; ssid_ucp_sso_v1=1.0.0-KGRlYmJhNzU4NzhiODc0MjFkYmRkYWE5MzljNjU4NmI0YjBlNGU4NmMKIQjb69H4g8ydAxCKua67BhjvMSAMMLvkj7AGOAZA9AdIBhoCbGYiIDI0NjNlYzAzMWQxYjg1YTgwYWRhNjkxYWM2MGMwYmQx; login_time=1735105672930; passport_auth_status=e4961065aab879e0597c13d61c7f395d%2C; passport_auth_status_ss=e4961065aab879e0597c13d61c7f395d%2C; uid_tt=375ca5256ffeaaa864c904a5e2a60d21; uid_tt_ss=375ca5256ffeaaa864c904a5e2a60d21; sid_tt=88c609a031facd3d2d0991341d4137e0; sessionid=88c609a031facd3d2d0991341d4137e0; sessionid_ss=88c609a031facd3d2d0991341d4137e0; is_staff_user=false; publish_badge_show_info=%220%2C0%2C0%2C1735105676522%22; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=2f385951e2486c2d07e66dafb8eeec9c; __security_server_data_status=1; sid_guard=88c609a031facd3d2d0991341d4137e0%7C1735105680%7C5183997%7CSun%2C+23-Feb-2025+05%3A47%3A57+GMT; sid_ucp_v1=1.0.0-KGIwMmZmYmMwZjE2ODVhMWY2Yzc1MDc3MTk4YWRlZTFkOGVjOTcwY2UKGwjb69H4g8ydAxCQua67BhjvMSAMOAZA9AdIBBoCaGwiIDg4YzYwOWEwMzFmYWNkM2QyZDA5OTEzNDFkNDEzN2Uw; ssid_ucp_v1=1.0.0-KGIwMmZmYmMwZjE2ODVhMWY2Yzc1MDc3MTk4YWRlZTFkOGVjOTcwY2UKGwjb69H4g8ydAxCQua67BhjvMSAMOAZA9AdIBBoCaGwiIDg4YzYwOWEwMzFmYWNkM2QyZDA5OTEzNDFkNDEzN2Uw; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1366%2C%5C%22screen_height%5C%22%3A768%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; download_guide=%222%2F20241225%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSmlOQ2JFT1lSZ0t1bzJVOXFzUGFLbGN2Smk5bUozdWJIbG5KNlhuTHo4NHJHT1gxb21vZmtoandXOXlWeitSK0JqRlNDNTU1T21YQ3BYVGg5a0ViWnM9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; odin_tt=9a5c81dbec34b262aced49be178561824841a64b5c0e7cc853bfbf0adeede6a114ae2b2f21a2e16c52907482a439175f; IsDouyinActive=false; passport_fe_beating_status=false',
            # Referer 防盗链，告诉服务器请求网址从哪里跳转过来的
            'Referer':'https://www.douyin.com/user/MS4wLjABAAAArcoz8pyUJSASISQnP_JMfUgNATaCTOJJzQsG6HSzeAU?from_tab_name=main&modal_id=7440465989214489882',
            # User-Agent 用户代理，表示浏览器、设备基本身份信息
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

        # 请求网址
        url = f'https://www.douyin.com/user/MS4wLjABAAAArcoz8pyUJSASISQnP_JMfUgNATaCTOJJzQsG6HSzeAU?from_tab_name=main&modal_id={video_id}'

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
        with open('video\\' + clean_filename(title) + '.mp4', mode='wb') as f:
            # 写入数据内容
            f.write(video_content)

    dp.scroll.to_bottom()