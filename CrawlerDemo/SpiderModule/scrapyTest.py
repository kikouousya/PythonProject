import requests
import bs4




url = "https://pic.qiushibaike.com/article/image/W4JHXN2NZ02K1EMG.jpg"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/69.0.3497.100 Safari/537.36"}
response = requests.post(url=url, headers=headers)

image_byte = response.content  # .content获取二进制数据

with open("img.jpg", "wb")as fp:  # 使用wb模式写入图片数据
    fp.write(image_byte)

url = "https://www.sogou.com"
response = requests.get(url, headers=headers)

# 创建soup对象, 第一个参数可以是文本或文件fp句柄
soup = bs4.BeautifulSoup(response.text, "lxml")

# soup.元素名称 定位到第一个对应的标签
print(soup.div)  # 定位到第一个div

# soup.find('标签名', 属性名='xx') 查找对应的标签; find返回第一个, find_all 返回全部
soup.find('div', class_= 'skin-bg')  # 查找class为skin-bg的div
soup.find('img', id="bg-img")  # 查找id为bg-img的img标签

tag_a = soup.find_all('a', name="wow")

# soup.select('css选择器') 选择器定位, 使用css选择器进行元素定位 返回列表
tag_div = soup.select('.skin-bg')  # 查找class为skin-bg的所有元素
tag_li = soup.select('.event-list > ul > li')  # 查找div(class=event-list) 里的ul 里的li元素(>表示儿子)
tag_li2 = soup.select('.event-list li')  # 查找div(class=event-list) 里的li元素 (空格表示子孙后代都行)

# 标签元素.string 获取自己文字 .text 获取子孙的所有文字
print(tag_div.string)  # 获取这个div中的文字
print(tag_div.text)  # 获取这个div和内部子孙的所有文字

# 标签元素['属性名'] 获取目标元素的属性值
print(tag_a['href'])   # 获取a标签中的href属性得知其链接



