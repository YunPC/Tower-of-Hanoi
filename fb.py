def fib (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    

if __name__ == '__main__':
    n = int(input('Type your number : '))
    print(fib(n))

