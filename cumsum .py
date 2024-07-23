def cumsum(numbers):
    cumulative_sum = [numbers[0]] if numbers else []
    
    for i in range(1, len(numbers)):
        next_element = numbers[i] + cumulative_sum[-1]
        
        cumulative_sum.append(next_element)
    
    return cumulative_sum


t = [1, 2, 3]
print(cumsum(t)) 


another_list = [1, 5, 7, 2, 9]
print(cumsum(another_list)) 