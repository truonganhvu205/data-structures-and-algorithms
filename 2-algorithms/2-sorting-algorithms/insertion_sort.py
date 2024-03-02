def insertion_sort(l):
    for i in range(1, len(l)):
        a = l[i]
        j = i - 1
        
        while j >= 0 and l[j] > a:
            l[j + 1] = l[j]
            j -= 1
            
        l[j + 1] = a

if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    insertion_sort(l)
    
    print(l)