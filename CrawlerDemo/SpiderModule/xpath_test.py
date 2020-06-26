from  lxml import etree

tree= etree.parse('result_page.html')

print(tree)

# 只有一个函数 tree.xpath(命令)
# '/html/标签1/标签2' 从根标签逐层查找  '//标签名' 从任意位置查找
tree.xpath('/html/head/title')  # 从根标签查找对应标签
tree.xpath('//title')  # 从任意地方查找
tree.xpath('//body/div//a') # 此时a可以是div的子孙

# 属性查找标签[@属性="值"]
tree.xpath('//div[@class="wow"]')
# 索引定位
tree.xpath('//li[@class="img-item"][2]')  # 取第n个li标签 注: 索引从1开始

# 取文本 /text()
tree.xpath('//p/text()')  # 获取该标签内的文本
tree.xpath('//p//text()')  # 获取子孙文本

# 取属性 /@属性名
tree.xpath('//a[@class="link-url"]/@href')  # 获取目标a标签内的href属性


# 相对路径问题
div = tree.xpath('//div[@class="main-content]"')
div.xpath('./ul/li')  # 这里要用 "." 表示从当前位置进行查找 否则报错

