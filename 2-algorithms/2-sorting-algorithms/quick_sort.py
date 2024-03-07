# HOARE PARTITION

def swap(a, b, lst):
    if a != b:
        lst[a], lst[b] = lst[b], lst[a]

def partition(head_index, tail_index, lst):
    pivot_index = head_index
    
    while head_index <= tail_index:
        while head_index < len(lst) and lst[head_index] <= lst[pivot_index]:
            head_index += 1
        while lst[tail_index] > lst[pivot_index]:
            tail_index -= 1
        if head_index < tail_index:
            swap(head_index, tail_index, lst)
            
    swap(pivot_index, tail_index, lst)
    return tail_index

def quick_sort(head_index, tail_index, lst):
    if head_index < tail_index:
        p = partition(head_index, tail_index, lst)
        quick_sort(p + 1, tail_index, lst)
        quick_sort(head_index, p - 1, lst)
    
if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    
    quick_sort(0, len(lst) - 1, lst)
    print(lst)