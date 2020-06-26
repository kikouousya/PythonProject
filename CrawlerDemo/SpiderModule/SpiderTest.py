import requests

url_search = "https://www.sogou.com/web"
# 自定义GET请求参数
params = {"ie": "UTF-8",
          "query": "爬虫"}

# 自定义请求头信息
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/69.0.3497.100 Safari/537.36"}

response = requests.get(url=url_search, params=params, headers=headers)  # 发起请求

# 储存网页
with open("./sogou_search.html", "w", encoding="utf-8") as fp:
    fp.write(response.text)