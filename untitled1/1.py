li = ['alex','egon','yuan','wusir','666']
# 把666替换成999
li[4]='999'
# 获取"yuan"索引
count = 0
for i in li:
    if i == 'yuan':
        print(count)
    count+=1
print(li.index('yuan'))
# 假设不知道前面有几个元素，得到最后的三个元素
print(li[-3:])