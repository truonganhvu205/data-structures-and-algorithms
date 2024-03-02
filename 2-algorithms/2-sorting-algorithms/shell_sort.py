def shell_sort(l):
    g = len(l) // 2
    
    while g > 0:
        for i in range(g, len(l)):
            a = l[i]
            j = i
            
            while j > 0 and l[j - g] > a:
                l[j] = l[j - g]
                j -= g
                
            l[j] = a
        g //= 2

if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    shell_sort(l)
    
    print(l)