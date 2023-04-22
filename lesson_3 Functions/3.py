def sum_numbers(n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
    print('stop') #return finishes the function

""" a = sum_numbers(5)
print(a) """
print(sum_numbers(5, 'qwert'))


def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'f', 'r'))
""" print(sum_str(1, 8, 9)) #error, int not str """

# MODULES

# Recursions

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)

list1 = []
for i in range(1, 10):
    list1.append(fib(i))
print(list1)