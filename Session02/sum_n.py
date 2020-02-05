# 1 + 2 + 3 + ... + 20
# 1 + ... + 100


def sum_n(n):
    res_n = 0
    for i in range(0, n):
        res_n += i + 1
    return res_n


print("Sum of the numbers 1-20 is:", sum_n(20))
print("Sum of the numbers 1-100 is:", sum_n(100))
