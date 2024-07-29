def is_sorted(lst):
    if not lst:
        return True
    
    if len(lst) == 1:
        return True
    
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False  
    
    return True  

print(is_sorted([]))                
print(is_sorted([1]))               
print(is_sorted([1, 2, 3]))         
print(is_sorted([1, 3, 2]))         
print(is_sorted([3, 2, 1]))         