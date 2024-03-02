def binary_search(l, f):
    h = 0
    t = len(l) - 1
    
    while h <= t:
        m = (h + t) // 2
        
        if l[m] == f:
            return m
        elif l[m] < f:
            h = m + 1
        else:
            t = m - 1
            
    return -1

if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    f = 5
    
    print(binary_search(l, f)) # 2