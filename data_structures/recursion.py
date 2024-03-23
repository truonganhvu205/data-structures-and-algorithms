def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n - 1)
    
'''
0, 1, 2, 3, 4, 5
----------------
0, 1, 1, 2, 3, 5
'''
    
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(sum(100))
    print(fib(5))