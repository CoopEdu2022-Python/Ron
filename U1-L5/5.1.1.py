# 5.1.1 为以下列表尝试以上 14 种方法 / 函数 / 关键字，每一步操作后，打印当前的列表
num_list = [1, 2, 3, 4, 5]
num_list.insert(0, 0)
print('step 0 :', num_list)
num_list.append(123)
print('step 1 :', num_list)
list2 = [999]
num_list.extend(list2)
print('step 2 :', num_list)
del num_list[0]
print('step 3 :', num_list)
del list2
print('step 4 :', num_list)#list2被删除了
num_list.remove(1)
print('step 5 :', num_list)
num_list.pop()
print('step 6 :', num_list)
num_list.pop(0)
print('step 6 :', num_list)
num_list.clear()
print('step 7 :', num_list)
num_list = [1, 2, 3, 4]
num_list[0]=2
print('step 8 :', num_list)
num_list.sort
print('step 9 :', num_list)
num_list.sort(reverse=True)
print('step 10 :', num_list)
num_list.reverse()
print('step 11 :', num_list)
len(num_list)
print('step 12 :', len(num_list))
num_list.count(2)
print('step 11 :', num_list.count(2))
