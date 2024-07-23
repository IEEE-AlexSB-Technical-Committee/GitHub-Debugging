import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def compute_polygon_perimeter():
    points = []
    
    x = input("Enter the x part of the coordinate: ")
    if x == "":
        return 0.0  
    y = float(input("Enter the y part of the coordinate: "))
    points.append((float(x), y))
    
    while True:
        x = input("Enter the x part of the coordinate: (blank to quit): ")
        if x == "":
            break
        y = float(input("Enter the y part of the coordinate: "))
        points.append((float(x), y))
    
    perimeter = 0.0
    for i in range(len(points)):
        next_i = (i + 1) % len(points)
        perimeter += calculate_distance(points[i][0], points[i][1], points[next_i][0], points[next_i][1])
    
    return perimeter

perimeter = compute_polygon_perimeter()
print(f"The perimeter of that polygon is {perimeter:.5f}")