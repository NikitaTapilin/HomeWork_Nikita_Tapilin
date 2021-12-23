nums = list(range(1000))
nums_main = []
for i in nums:
    if not i % 2 == 0:
        nums_main.append(i ** 3)

sum_first = []
sum_digits = 0
for i in nums_main:
    num = i
    while i != 0:
        sum_digits = sum_digits + i % 10
        i = i // 10
    if sum_digits % 7 == 0:
        sum_first.append(num)
    sum_digits = 0

print(sum(sum_first))

sum_second = []
sum_digits = 0
for i in nums_main:
    num = i
    i += 17
    while i != 0:
        sum_digits = sum_digits + i % 10
        i = i // 10
    if sum_digits % 7 == 0:
        sum_second.append(num)
    sum_digits = 0

print(sum(sum_second))
