xiaoming = {"name":"xiaoming",
            "age":"18",}
#取值
print(xiaoming["name"])
#增加/修改
xiaoming["A"] = 18
print(xiaoming)
xiaoming["name"] = "小小明"
print(xiaoming)
#删除
xiaoming.pop("name")
print(xiaoming)
#统计键值对数量
print(len(xiaoming))
#合并字典
tem = {"height":1.75}
xiaoming.update(tem)
print(xiaoming)
#清空字典
# xiaoming.clear()
# print(xiaoming)
for k in xiaoming:
    print("%s - %s"%(k,xiaoming[k]))
card_list = [{
    "name":"张三"
}]

for c in card_list:
    print(card_list)