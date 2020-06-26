from selenium import webdriver

# 配置浏览器路径
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Users\ASUS\AppData\Local\CentBrowser\Application\chrome.exe"
# options.add_argument('--headless')  # 隐藏浏览器界面
# options.add_argument('--disable-gpu')  # 不使用gpu渲染
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # webdriver伪装
# 使用chromedirver操作谷歌浏览器
browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

browser.get('https://www.aqistudy.cn/')

with open('localSite.html', 'w', encoding='utf8') as fp:
    fp.write(browser.page_source)