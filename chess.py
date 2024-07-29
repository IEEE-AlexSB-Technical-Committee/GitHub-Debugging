def determine_square_color(position):
    column_index = ord(position[0].lower()) - 97
    row_index = int(position[1]) - 1
    
    if (column_index + row_index) % 2 == 0:
        return "white"
    else:
        return "black"

position = input("Enter a chess position (e.g., 'a1', 'd5'): ")
square_color = determine_square_color(position)
print(f"The square at position {position} is {square_color}.")