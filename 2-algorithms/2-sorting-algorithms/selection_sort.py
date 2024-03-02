def selection_sort(l):
    for i in range(len(l) - 1):
        m = i
        
        for j in range(m + 1, len(l)):
            if l[m] > l[j]:
                m = j
                
        if m != i:
            l[m], l[i] = l[i], l[m]

if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    selection_sort(l)
    
    print(l)