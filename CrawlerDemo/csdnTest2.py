import requests
from lxml import etree
import os
def getResponse(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Connection': 'close'}
    try:
        r = requests.get(url, headers=header, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        return 0
def ResponseParse(r, alist):
    if r:
        dom = etree.HTML(r.text)
        articles_xpath = './/div[@class="container clearfix pt0"]/main/div[@class="article-list"]'
        articeles = dom.xpath(articles_xpath)
        title_xpath = './/div[@class="article-item-box csdn-tracking-statistics"]/h4/a/text()'
        type_xpath = './/div[@class="article-item-box csdn-tracking-statistics"]/h4/a/span/text()'
        href_xpath = './/div[@class="article-item-box csdn-tracking-statistics"]/p[@class="content"]/a/@href'
        abstract_xpath  = './/div[@class="article-item-box csdn-tracking-statistics"]/p[@class="content"]/a/text()'
        date_xpath = './/div[@class="article-item-box csdn-tracking-statistics"]/div/p[1]/span[@class="date"]/text()'
        read_xpath = './/div[@class="article-item-box csdn-tracking-statistics"]/div/p[3]/span[@class="read-num"]/span[@class="num"]/text()'
        comment_xpath = './/div[@class="article-item-box csdn-tracking-statistics"]/div/p[5]/span[@class="read-num"]/span[@class="num"]/text()'
        for article in articeles:
            title = article.xpath(title_xpath)
            type = article.xpath(type_xpath)
            href = article.xpath(href_xpath)
            abstract = article.xpath(abstract_xpath)
            date = article.xpath(date_xpath)
            read = article.xpath(read_xpath)
            comment = article.xpath(comment_xpath)
        for i in range(len(type)):
            alist.append([title[2*i + 1].strip().replace("\n", ""), type[i], href[i], abstract[i].strip().replace("\n", ""), date[i].strip().replace("\n", ""), read[i], comment[i]])
            print("文章标题：" + title[2*i + 1].strip().replace("\n", ""))
            print("文章类型：" + type[i])
            print("文章链接：" + href[i])
            print("文章摘要：" + abstract[i].strip().replace("\n", ""))
            print("发布时间：" + date[i].strip().replace("\n", ""))
            print("阅读数：" + read[i])
            print("评论数：" + comment[i])
            print("\n")
        return len(type)
    else:
        print("爬取失败！")

def Get_article_count(url):
    #//*[@id="asideProfile"]/div[2]/dl[1]/dd/a/span
    #/html/body/div[2]/div[1]/div[2]/ul/li[1]/a/label/span[2]
    #/html/body/div[2]/div[1]/div[2]/ul/li[1]/a/label/span[2]
    r = getResponse(url)
    print(r.url)
    # print(r.text)
    dom = etree.HTML(r.text)
    count_xpath1 = './/html/body/div[2]/div[1]/div[2]/ul/li[1]/a/label/span[2]/text()'
    count_xpath = './/div[@class="me_chanel_bar clearfix"]/ul/li/a[@class="tab_item tab_item_click"]/label/span[2]/text()'
    article_count = dom.xpath(count_xpath)
    return int(article_count[0].strip().replace("\n", ""))
def Get_author_name(url):
    #/html/body/div[2]/div[1]/div[1]/div[2]/p/text()
    r = getResponse(url)
    dom = etree.HTML(r.text)
    name_xpath = './/div[@class="me_wrap_lt clearfix"]/div[@class="lt_main clearfix"]/p[@class="lt_title"]/text()'
    name = dom.xpath(name_xpath)[2].strip().replace("\n", "")
    print("作者：", str(name))
    return name


def WriteWord(alist, name):
    save_dir = '文章列表'
    save_dir = os.path.join(os.getcwd(), save_dir)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    save_name = os.path.join(save_dir, name)
    out = "文章标题：{0:{7}<10}\n文章类型：{1:{7}<10}\n文章链接：{2:{7}<20}\n文章摘要: {3:{7}<10}\n发布时间：{4:{7}<10}\n阅读数：{5:{7}<10}\n评论数：{6:{7}<10}\n"
    with open(save_name, 'w', encoding="utf-8") as f:
        for i in range(len(alist)):
            f.write(out.format(alist[i][0], alist[i][1], alist[i][2], alist[i][3], alist[i][4], alist[i][5], alist[i][6], chr(12288)))
            f.write("\n")
        f.close()
    print("数据成功写入："+save_name)

def main():
    try:
        article_list = []
        user_name = "fovever_" #再次修改查询的用户名称https://blog.csdn.net/fovever_一般为用户主页最后一个下划线后的字符串
        url1 = "https://{0}.csdn.net/{1}"
        url = url1 + '/article/list/{2}'
        article_count = Get_article_count(url1.format("me", user_name))
        save_name = Get_author_name(url1.format("me", user_name)) + '.doc'
        if article_count % 40 == 0:
            spider_num = article_count /40
        else:
            spider_num = article_count / 40 + 1
        print(article_count)
        spider_article_count = 0
        for i in range(int(spider_num)):
            r = getResponse(url.format("blog", user_name, str(i + 1)))
            spider_article_count += ResponseParse(r, article_list)
        WriteWord(article_list, save_name)
        print("共爬取了：" + str(spider_article_count) + "篇博客！")
    except:
        print(user_name+"博客爬取失败！")


if __name__ == '__main__':
    main()
