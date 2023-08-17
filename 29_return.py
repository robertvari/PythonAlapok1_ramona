def add_numbers(a, b):
    return a+b

def multiply_numbers(a, b):
    return a*b

def divide_numbers(a, b):
    return a/b


result_add = add_numbers(100, 50)
result_multiply = multiply_numbers(result_add, 10)
result_divide = divide_numbers(result_multiply, 100)
print(result_divide)