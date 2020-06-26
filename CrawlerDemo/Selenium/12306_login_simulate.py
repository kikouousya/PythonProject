from time import sleep

import PIL
from PIL import Image
from selenium import webdriver


# 配置浏览器路径
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Users\ASUS\AppData\Local\CentBrowser\Application\chrome.exe"
options.add_argument('--headless')  # 隐藏浏览器界面
options.add_argument('--disable-gpu')  # 不使用gpu渲染
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # webdriver伪装
# 使用chromedirver操作谷歌浏览器
browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

# 开始浏览器脚本
browser.get('https://kyfw.12306.cn/otn/login/init')  # 进入12306网页
sleep(1.5)

# 截图当前页面的验证码, 发送给打码平台; 不能去下载, 因为每次下载返回新的随机验证码

code_img_tag = browser.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
# 把整个屏幕截图并存起来
browser.save_screenshot('Screen.png')

# 裁剪这张图片发到打码平台
location = code_img_tag.location  # 获取图片标签的坐标(注: 获取的是左下角的坐标)
size = code_img_tag.size  # 获取标签的长宽
rectangle = (int(location['x']),
             int(location['y']),
             int(location['x']+size['width']),
             int(location['y']+size['height']))
# 使用PIL 的Image进行图片裁剪
i = Image.open('Screen.png')
cropped = i.crop(rectangle)  # 使用上面的矩形范围进行裁剪
cropped.save('Code.png')  # 储存

##### 将图片发送带你的打码平台 #####
# result = "50,70|267,133"  # 模拟返回的结果
result = input('模拟打码平台获得的坐标序列')
####################################

# 处理返回的字符串, 变成一个点的列表
result_list = []  # 最终结果的点
point_list = result.split('|')
for i in point_list:
    x , y = i.split(',')
    result_list.append({'x': int(x),'y': int(y)})

# 挨个点击验证码答案
chain = webdriver.ActionChains(browser)
for i in result_list:
    chain.move_to_element_with_offset(code_img_tag, i['x'], i['y'])
    chain.click().perform()
    sleep(1)
browser.find_element_by_id('username').send_keys('123456')
browser.find_element_by_id('password').send_keys('123456')
browser.find_element_by_id('loginSub').click()

print(browser.page_source)