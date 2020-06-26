import requests

url = "https://i.csdn.net/"
url = "https://blog.csdn.net/fovever_/article/details/104174560"
cookies = "uuid_tt_dd=10_19030098370-1587701249997-406534; dc_session_id=10_1587701249997.927265; dc_sid=7cb3108c2ad4cf0b070b4816f3e22570; __gads=ID=69313c748bc83c61:T=1587908776:S=ALNI_MaEgYS7xWQFqEBSr1ilqh98rr7u7Q; c_first_ref=www.baidu.com; SESSION=a5de8c29-09e4-482f-86c7-fc768ba12a6d; UserName=zui130; UserInfo=eb160b99bafc48b3a83705ab8f62a9ae; UserToken=eb160b99bafc48b3a83705ab8f62a9ae; UserNick=zui130; AU=D9A; UN=zui130; BT=1591254525419; p_uid=U100000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22zui130%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19030098370-1587701249997-406534!5744*1*zui130; c_utm_source=blogxgwz8; aliyun_webUmidToken=T27098823925B58D70960B642F38566B51862828FE852FD08771453ADF7; c_ref=https%3A//www.baidu.com/link; c_first_page=https%3A//www.csdn.net/; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1592840364,1592840394,1592846317,1593000640; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fmarketing.csdn.net%252Fp%252F00839b3532e2216b0a7a29e972342d2a%253Futm_source%253D618%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; c_adb=1; c_page_id=https%3A//i.csdn.net/%23/account/index; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1593000647; dc_tos=qcfj61"
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
headers = {
    'User-Agent': user_agent,
    'Cookies': cookies
}

responce = requests.get(url=url, headers=headers)
# responce = requests.get(url=url)

text = responce.text

with open("result.html", 'w', encoding='utf-8') as fp:
    fp.write(text)



