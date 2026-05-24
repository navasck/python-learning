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