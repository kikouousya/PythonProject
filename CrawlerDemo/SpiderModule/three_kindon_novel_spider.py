import requests
import bs4
import os

site_url = 'http://www.shicimingju.com/book/sanguoyanyi.html'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/69.0.3497.100 Safari/537.36"}

page_text =requests.get(site_url, headers=headers).text

soup = bs4.BeautifulSoup(page_text, 'lxml')

# print(soup)
if not os.path.exists('sanguoyanyi'):
    os.mkdir('sanguoyanyi')

title_a_tags = soup.select('.book-mulu > ul > li > a')
for a_tag in title_a_tags:
    title = a_tag.string
    article_url = 'http://www.shicimingju.com' + a_tag['href']
    # print(title, article_url)
    article_page_text = requests.get(article_url, headers=headers).text
    article_soup = bs4.BeautifulSoup(article_page_text, 'lxml')
    article_content = article_soup.select('.bookmark-list>.chapter_content')[0].text
    with open('sanguoyanyi/%s.txt' % title, 'w', encoding='utf-8')as fp:
        fp.write(article_content)




