def test(*params):
    for param in params:
        print(param)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

test("строка", 321, [1, 2, 3])
print(factorial(6))