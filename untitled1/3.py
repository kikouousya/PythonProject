d = {
       "Development":"开发小哥",
        "OP":"运维小哥",
        "Operate":"运营小仙女",
        "UI":"UI小仙女"
    }


# 增加： name : alex
d['name'] = 'alex'
# 修改： alex  改为 wusir
d['name'] =  'wusir'
# 删除： 删除 name 为 wusir
d.pop('name')
# 查询： "UI":"UI小仙女"
d.get('UI')
