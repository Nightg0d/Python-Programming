def multiply(a, b):
    result = 0
    for i in range(b):
        result = result + a
    print(result)
multiply(5, 4)


def multiply(a, b):
    if b == 1:
        return a
    return a + multiply(a, b - 1)
print(multiply(3, 4))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(6))



def palin(text):
    if len(text) <= 1:
        print("palindrome")
    else:
        if text[0] == text[-1]:
            palin(text[1:-1])
        else:
            print("Not a palin")

palin("madam")
palin("malayalam")
palin("python")
palin("abba")


def fib(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fib(m - 1) + fib(m - 2)
print(fib(12))


def memo(m, d):
    if m in d:
        return d[m]
    else:
        d[m] = memo(m - 1, d) + memo(m - 2, d)
        return d[m]
d = {0: 1, 1: 1}
print(memo(48, d))