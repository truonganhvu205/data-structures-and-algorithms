# HOARE PARTITION

def swap(a, b, l):
    if a != b:
        l[a], l[b] = l[b], l[a]

def partition(h, t, l):
    p = h
    
    while h <= t:
        while h < len(l) and l[h] <= p:
            h += 1
        while l[t] > p:
            t -= 1
            
        if h < t:
            swap(h, t, l)
            
    swap(p, t, l)
    return t

def quick_sort(h, t, l):
    if h < t:
        p = partition(h, t, l)
        quick_sort(h, p - 1, l)
        quick_sort(p + 1, t, l)

if __name__ == '__main__':
    l = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    quick_sort(0, len(l) - 1, l)
    
    print(l)