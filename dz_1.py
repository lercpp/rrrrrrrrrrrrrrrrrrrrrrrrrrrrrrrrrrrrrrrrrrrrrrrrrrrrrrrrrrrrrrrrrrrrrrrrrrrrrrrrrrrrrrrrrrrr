def sum_of_abs(numbers):
    sum=0
    for i in range(len(numbers)):
        sum+=numbers[i]

    return sum

print(sum_of_abs([1, -2, 3, -4])) # 10
print(sum_of_abs([-5])) # 5
print(sum_of_abs([])) # 0

def count_positive(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            count += 1

    return count

print(count_positive([1, -2, 3, 0, 5])) # 3
print(count_positive([-1, -2])) # 0
print(count_positive([])) # 0

def apply_and_collect(lst, func):
    a = []
    for i in range(len(lst)):
        lst[i] = func()
        a.append(lst[i])

    return a

print(apply_and_collect([1, 2, 3], lambda x: x + 1)) # [2, 3, 4]
print(apply_and_collect([2, 4, 6], lambda x: x // 2)) # [1, 2, 3]


def keep_non_zero(numbers):
    a = []
    for i in range(len(numbers)):
        if numbers[i] != 0:
            a.append(numbers[i])

    return a

print(keep_non_zero([0, 1, 0, 2, 3])) # [1, 2, 3]
print(keep_non_zero([0, 0])) # []


def all_true(lst, pred):
    for i in range(len(lst)):
        if lst[i] == pred():
            return True
        
    return False

print(all_true([2, 4, 6], lambda x: x % 2 == 0)) # True
print(all_true([2, 3, 6], lambda x: x % 2 == 0)) # False
print(all_true([], lambda x: x > 0)) # True


def print_with_index(lst):
    for i in range(len(lst)):
        print(lst[i],i)

print_with_index(["a", "b", "c"])
# 0: a
# 1: b
# 2: c


def count(lst, pred):
    count = 0
    for i in range(len(lst)):
        if lst[i] == pred():
            count += 1
    return count

print(count([1, 2, 3, 4], lambda x: x == 3)) # 1
print(count([1, 2, 3], lambda x: x % 2 == 1 or x == 2)) # 2
print(count([], lambda x: x ** 2 > 100)) # 0

def take_while(lst, pred):
    #чего...