def remove_extremes(sorted_list, n):
    if len(sorted_list) < 4:
        return "Error: Please enter at least 4 values."
    
    
    sorted_list = sorted_list[:-n]
    
    sorted_list = sorted_list[n:]
    

    return sorted_list


sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
print(remove_extremes(sorted_list, n))  


short_list = [1, 2, 3]
print(remove_extremes(short_list, n)) 