def binary_search(lst, find):
    head_index = 0
    tail_index = len(lst) - 1
    
    while head_index <= tail_index:
        mid_index = (head_index + tail_index) // 2
        
        if lst[mid_index] == find:
            return mid_index
        elif lst[mid_index] < find:
            head_index = mid_index + 1
        else:
            tail_index = mid_index - 1
            
    return -1

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    find = 5
    
    print(binary_search(lst, find))