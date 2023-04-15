list_1 = []
list_1 = list()

list_1 = [1, 2, 3, 8]

for i in list_1:
    print(i)

print()

print(len(list_1))
print(list_1[0])

print()

list_2 = [1, 5]
print(list_2)
list_2.append(8)
print(list_2)

print()


list_3 = []
for i in range(5):
    list_3.append(i)
    print(list_3)

print()

# delete the last element:
list_4 = [12, 7, -1, 21, 0]
print(list_4.pop())  # 0
print(list_4)

print()

# delete the specific element:
list_5 = [12, 7, -1, 21, 0]
print(list_5.pop(0))  # 12
print(list_5)

print()

# adding the element to the nec index
list_6 = [12, 7, -1, 21, 0]
print(list_6.insert(2, 11))  # ind, the number
print(list_6)

print()

# КОРТЕЖИ
t = ()
print(type(t))  # tuple

t = (1)
print(type(t))  # int

t = (1,)
print(type(t))  # tuple

print()

v = [1, 8, 9]
print(v)
print(type(v))  # list

v = tuple(v)
print(v)
print(type(v))  # tuple

a, b, c = v

print(a, b, c)

print()

# КОТРТЕЖ ТО ЖЕ САМОЕ ЧТО И СПИСОК, НО ИЗМЕНЯТЬ НЕЛЬЗЯ
t = (1, 2, 3, 5,)

for i in range(len(t)):
    print(t[i])

""" t[0] = 2  # error """
print()

# СЛОВАРИ
d = {}
d = dict()

d['q'] = 'qwerty'
print(d) # 'q': 'qwerty'

d['w'] = 'werty'
print(d) #'q': 'qwerty', 'w': 'werty'
print(d['q']) #qwerty


