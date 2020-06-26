from selenium.webdriver import ActionChains
from selenium import  webdriver


# 配置浏览器路径
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Users\ASUS\AppData\Local\CentBrowser\Application\chrome.exe"

# 使用chromedirver操作谷歌浏览器
browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

# 开始浏览器脚本
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')  # 测试页面
browser.switch_to.frame('iframeResult')  # 如果元素在iframe中, 则要先switch进去
div_tag = browser.find_element_by_id('draggable')
print(div_tag)

# 创建动作链
chain = ActionChains(browser)
chain.click_and_hold(div_tag)  # 点击目标元素
for i in range(10):
    chain.move_by_offset(0, 10).perform()  # 移动到相对位置, 每次向下移动10个像素

chain.release()  # 把动作链释放掉


