def fibonacci(n, m):
    fib = '1'
    fib_line = list(fib * m)
    i = 2   
    while i < len(fib_line):
        fib_line[i] = int(fib_line[i - 1]) + int(fib_line[i - 2])
        i += 1

    print(fib_line)
    print(len(fib_line))
    print(type(fib_line))

print(fibonacci(1,5))