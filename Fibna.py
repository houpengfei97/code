def fib(n):
    # if n < 2:
    #     return n
    # else:
    #     return fib(n-1)+fib(n-2)

    f=0
    g=1
    while (0 < n):
        g = g+f
        f = g-f
        n-=1
    return g
if __name__ == '__main__':
    for i in range(1,10):
        print (fib(i))