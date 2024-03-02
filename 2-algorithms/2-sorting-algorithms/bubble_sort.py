def bubble_sort(l):
    for i in range(len(l) - 1):
        s = False
        
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                s = True
                
        if not s:
            break

if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    bubble_sort(l)
    
    print(l)