def linear_search(lst, find):
    for index, number in enumerate(lst):
        if number == find:
            return index
            
    return -1

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    find = 5
    
    print(linear_search(lst, find))