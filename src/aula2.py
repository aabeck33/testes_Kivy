lista_nums = [100,200,300,400]
for item in range(len(lista_nums)):
    lista_nums[item] += 1000
print(lista_nums)


lista_nums = [100,200,300,400]
for idx,item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)

i = 10
lista_nums2=[]
for i in range(i+1):
    lista_nums2.append(i)

lista_nums2.insert(4,100)

print(lista_nums2)
print(lista_nums2[2])
print(lista_nums2[3:7+1:2])
print(lista_nums2[2:])
print(lista_nums2[:2+1])
print(lista_nums2[::3])

lista_nums2.reverse()
print(lista_nums2)
lista_nums2.sort(reverse=True)
print(lista_nums2)
lista_nums2.sort()
print(lista_nums2)

print(lista_nums2.count(100))
print(lista_nums2.index(100))

print(len(lista_nums2))

print(lista_nums2[::-1])
print(lista_nums2[8:2:-1])
lista_nums2.pop(3)
print(lista_nums2)
del(lista_nums2[2:6:2])
print(lista_nums2)
lista_nums2.clear()
print(lista_nums2)
