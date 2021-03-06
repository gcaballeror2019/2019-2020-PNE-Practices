# -- Session 2, Ex 2
# -- Calculate the 5th, 10th and 15th terms of the Fibonacci series


def fibo_n(n):
    value_0 = 0
    value_1 = 1
    for i in range(0, n):
        n_val = value_1 + value_0
        value_0 = value_1
        value_1 = n_val
    return value_0


print("5th Fibonnaci term:", fibo_n(5))
print("10th Fibonnaci term:", fibo_n(10))
print("15th Fibonnaci term:", fibo_n(15))
