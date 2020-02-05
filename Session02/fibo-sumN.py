# -- Session 2, Ex 3
# -- Calculate the sumatory of the first 5 and 10 numbers of the Fibonacci series


def fibosum(n):
    value_0 = 0
    value_1 = 1
    result = 0
    for i in range(0, n):
        n_val = value_1 + value_0
        value_0 = value_1
        value_1 = n_val
        result += value_0
    return result


# -- We print the results


print("The sum of the first 5 terms of the Fibonacci series is:", fibosum(5))
print("The sum of the first 10 terms of the Fibonacci series is:", fibosum(10))
