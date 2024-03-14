def merge_two_sort(lst_i, lst_j, lst_k):
    i = j = k = 0
    
    while i < len(lst_i) and j < len(lst_j):
        if lst_i[i] < lst_j[j]:
            lst_k[k] = lst_i[i]
            i += 1
        else:
            lst_k[k] = lst_j[j]
            j += 1
            
        k += 1
        
    while i < len(lst_i):
        lst_k[k] = lst_i[i]
        i += 1
        k += 1
        
    while j < len(lst_j):
        lst_k[k] = lst_j[j]
        j += 1
        k += 1

def merge_sort(lst):
    if len(lst) <= 1:
        return
    
    mid_index = len(lst) // 2
    
    head_lst = lst[:mid_index]
    tail_lst = lst[mid_index:]
    
    merge_sort(head_lst)
    merge_sort(tail_lst)
    
    merge_two_sort(head_lst, tail_lst, lst)
    
if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    
    merge_sort(lst)
    print(lst)