def binary_search_recursive(l, f, h, t):
    if h > t:
        return -1
    
    m = (h + t) // 2
    
    if m < 0 or m > len(l):
        return -1
    
    if l[m] == f:
        return m
    elif l[m] < f:
        h = m + 1
    else:
        t = m - 1
    
    return binary_search_recursive(l, f, h, t)

if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    f = 5
    
    print(binary_search_recursive(l, f, 0, len(l) - 1)) # 2