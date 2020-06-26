from time import sleep

from selenium import webdriver


# 初始化浏览器对象

# 配置浏览器路径
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Users\ASUS\AppData\Local\CentBrowser\Application\chrome.exe"

# 使用chromedirver操作谷歌浏览器
browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

# 开始浏览器脚本
browser.get('https://www.jd.com')  # 登录京东
search_input = browser.find_element_by_xpath('//*[@id="key"]')  # 找到搜索框
search_input.send_keys('Nintendo Switch')  # 在输入框中输入Nintendo Switch
commit_btn = browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')  # 确认键
commit_btn.click()  # 点击确认键

sleep(2)
# 执行js代码
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 往下滚动一屏页面


# 获取page源码
print(browser.page_source)
sleep(5)

browser.quit()  # 退出浏览器