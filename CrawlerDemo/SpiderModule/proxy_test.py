import requests
from lxml import etree
import json
from multiprocessing.dummy import Pool, Lock
import random
import time


REFRESH_PROXY_LIST = False
VALUATE_PROXY = True


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/69.0.3497.100 Safari/537.36",
           "Connection": "close"  # 执行完毕后立刻断开请求连接 否则会导致http连接池爆满
           }

if REFRESH_PROXY_LIST:
    proxy_list = []

    #  爬取快代理的代理列表

    def get_proxy(i):
        try:
            print(i, 'in')
            page_text = requests.get('https://www.kuaidaili.com/free/inha/%d/'%i, headers=headers).text
            # print(page_text)
            tree = etree.HTML(page_text)
            print(tree.xpath('.//text()'))
            tr_list = tree.xpath('//*[@id="list"]//tr')[1:]  # tbody一定不能出现在xpath中 非常奇怪
            # print(tr_list)
            for tr in tr_list:
                ip = tr.xpath('./td[1]/text()')[0]
                port = tr.xpath('./td[2]/text()')[0]
                anonymity = tr.xpath('./td[3]/text()')[0]
                http_type = tr.xpath('./td[4]/text()')[0]
                print(i, ip, port, anonymity, http_type)
                proxy_list.append({http_type.lower(): "%s:%s" % (ip, port), 'anonymity': anonymity , 'id': i })
            time.sleep(0.9)  # 网站设置每台机器每秒只能发送1次请求
        except Exception as e:
            print(e)
        # break
    pool = Pool(1)
    pool.map(get_proxy, range(1,100))
    # for i in range(1, 200):
    #     get_proxy(i)



    with open('proxies.json', 'w', encoding='utf8') as fp:
        json_data = json.dumps(proxy_list)
        fp.write(json_data)
else:
    with open('proxies.json', 'r', encoding='utf-8') as fp:
        proxy_list = json.load(fp)

print('Total Proxy', len(proxy_list))

if VALUATE_PROXY:
    available_proxy_list = []
    lock = Lock()  # 进程锁
    with open('available_proxies.json', 'w', encoding='utf-8') as fp:
        json_data = json.dumps([])
        fp.write(json_data) # 清空文件数据
    def check_available(proxy):
        try:
            print('checking: ', proxy)
            response = requests.get('http://www.baidu.com', headers=headers, proxies=proxy, stream=True )  # stream防止奇怪的错误

            if response.status_code == 200:
                lock.acquire()  # 进程锁启用
                with open('available_proxies.json', 'r', encoding='utf8') as fp:
                    available_proxy_list = json.load(fp)
                available_proxy_list.append(proxy)
                with open('available_proxies.json', 'w', encoding='utf-8') as fp:
                    json_data = json.dumps(available_proxy_list)
                    fp.write(json_data)
                print('available proxy: ', proxy)
                lock.release()  # 进程锁释放
            else:
                print('not available proxy: ', proxy)

        except Exception as e:
            print(e)
    pool = Pool(200)
    pool.map(check_available, proxy_list)
    with open('available_proxies.json', 'w', encoding='utf-8') as fp:
        json_data = json.dumps(available_proxy_list)
        fp.write(json_data)
else:
    with open('available_proxies.json', 'r', encoding='utf8') as fp:
        available_proxy_list = json.load(fp)

print('Total available: ', len(available_proxy_list))