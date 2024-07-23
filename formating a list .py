def format_list(lst):
    if not lst:  
        return ""
    if len(lst) == 1:  
        return lst[0]

    
    items_except_last = ", ".join(lst[:-1])

    return f"{items_except_last}, and {lst[-1]}"


my_list = ["apple", "banana", "cherry", "date"]
print(format_list(my_list)) 

another_list = ["item1", "item2", "item3", "item4", "item5", "item6"]
print(format_list(another_list))  


empty_list = []
print(format_list(empty_list))  

single_item_list = ["single item"]
print(format_list(single_item_list))