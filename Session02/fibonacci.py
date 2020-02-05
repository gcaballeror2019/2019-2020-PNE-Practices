# -- Session 2, Ex 1
# -- Calculate the first eleven numbers of the Fibonacci serie

# -- We define two variables to manage the values in the  Fib. serie


value_0 = 0
value_1 = 1

for i in range(0, 11):
    print(value_0, end=" ")
    n_val = value_1 + value_0
    value_0 = value_1
    value_1 = n_val
