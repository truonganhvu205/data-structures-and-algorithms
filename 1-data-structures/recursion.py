def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

if __name__ == '__main__':
    print(sum(100))