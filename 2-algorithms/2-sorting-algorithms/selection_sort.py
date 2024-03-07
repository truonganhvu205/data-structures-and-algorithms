def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_index = i
        
        for j in range(min_index + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
                
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]
    
if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    
    selection_sort(lst)
    print(lst)