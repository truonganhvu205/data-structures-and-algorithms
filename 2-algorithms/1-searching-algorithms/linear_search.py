def linear_search(l, f):
    for i, e in enumerate(l):
        if e == f:
            return i
        
    return -1

if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    f = 5
    
    print(linear_search(l, f))