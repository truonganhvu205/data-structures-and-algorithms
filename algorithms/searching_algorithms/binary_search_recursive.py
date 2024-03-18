def binary_search_recursive(lst, head_index, tail_index, find):
    if head_index > tail_index:
        return -1
        
    mid_index = (head_index + tail_index) // 2
    
    if mid_index < 0 or mid_index > len(lst):
        return -1
        
    if lst[mid_index] == find:
        return mid_index
    elif lst[mid_index] < find:
        head_index = mid_index + 1
    else:
        tail_index = mid_index - 1
        
    return binary_search_recursive(lst, head_index, tail_index, find)
    
if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    find = 5
    
    print(binary_search_recursive(lst, 0, len(lst), find))