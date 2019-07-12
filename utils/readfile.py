#-*- coding: utf-8 -*-

# with open("/Users/saicao/Desktop/testPhone.txt") as files:
#
#     phoneList = files.readlines()
#
#     linesCounts = len(phoneList)
#
#     ll =  range(0, linesCounts, 500)
#
#     for key,value in enumerate(ll):
#         print key,len(ll)
#         if key < len(ll)-1:
#             print value,ll[key+1]
#             print phoneList[value:ll[key+1]]


def list_of_groups(init_list, children_list_len):
    list_of_groups = zip(*(iter(init_list),) *children_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % children_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list


def add(a, b):
    return a+b

# 列表前加一个星
list1 = [1, 2]
print(add(*list1))

# 字典前添加两个星
dict1 = {'a':1, 'b':2}
print(add(**dict1))
print(add(*dict1))

# tuple前使用*
tuple1 = (1, 2)
print(add(*tuple1))




