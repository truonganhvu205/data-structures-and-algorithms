def merge_two_sort(li, lj, lk):
    i = j = k = 0
    
    while i < len(li) and j < len(lj):
        if li[i] < lj[j]:
            lk[k] = li[i]
            i += 1
        else:
            lk[k] = lj[j]
            j += 1
            
        k += 1
        
    while i < len(li):
        lk[k] = li[i]
        i += 1
        k += 1
        
    while j < len(lj):
        lk[k] = lj[j]
        j += 1
        k += 1

def merge_sort(l):
    if len(l) <= 1:
        return
    
    m = len(l) // 2
    h = l[:m]
    t = l[m:]
    
    merge_sort(h)
    merge_sort(t)
    
    merge_two_sort(h, t, l)

if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    merge_sort(l)
    
    print(l)