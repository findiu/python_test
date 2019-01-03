#集合:无序，唯一
list_1 = [2, 4, 5, 5, 6, 7, 8, 1]
list_1 = set(list_1)
list_2 = set([2, 5, 9, 10, 11])
print(list_1, list_2)
print(list_1.intersection(list_2))#交集
print(list_1.union(list_2))#并集
print(list_1.difference(list_2))#差集
print(list_2.difference(list_1))#差集
#list_3 = {2, 4}
#list_3 = set([2, 4])
list_3 = set((2, 4))
print(list_3.issubset(list_1))#子集
print(list_1.issuperset(list_3))#父集
print(list_2.symmetric_difference(list_1))#把交集去掉,对称差集
list_4={3,5,7,2}
print(list_3.isdisjoint(list_4))
print(type(list_4))
print(list_1 & list_2)
print(list_1 | list_2)
print(list_1 - list_2)
print(list_1 ^ list_2)
print(list_1.add(11))
list_1.update([12,23])
print(list_1)
list_1.remove(2)
list_1.pop()
print(list_1)

