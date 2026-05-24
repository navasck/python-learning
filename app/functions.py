def greet(name):
    return f"Hello {name}"


message = greet("Abdul")

print(message)


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))
print(check_even_odd(8))



def format_name(first, last):
    return f"{first} {last}".upper()

print(format_name("Abdul", "Navas"))



def math_ops(a, b):
    return a + b, a - b, a * b

add, sub, mul = math_ops(10, 5)

print(add)
print(sub)
print(mul)


def sum_list(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(sum_list([1, 2, 3, 4]))



def transform(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return x + 2
    else:
        return 0

print(transform(5))
print(transform(-3))
print(transform(0))


def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-5))