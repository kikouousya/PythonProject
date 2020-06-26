import selenium

from selenium import webdriver

browser = webdriver.Chrome()

url = "https://www.csdn.net/"

browser.get(url)


with open("SeleniumPage.html", 'w', encoding='utf-8') as fp:
    fp.write(browser.page_source)