import math
def circle_area (r):
    if r < 0:
        return "Radius can't be negative"
    return math.pi * (r ** 2)

def triangle_area (b, h):
    if b < 0 or h < 0:
        return "Base and height cannot be negative."
    triangle2 = 0.5 * b * h
    return triangle2

def main():
    print("Choose a shape to calculate the area for:")
    print("1. Circle")
    print("2. Triangle")
    print("3. Circle and Triangle both")
    try:
        choice = int(input("Choose 1, 2 or 3(both): "))
        if choice == 1:
            print("Calculate the Area of Circle: ")
            radius  = float(input("Enter the radius: ")) 
            area = circle_area(radius)
            print(area)

        elif choice == 2:
            print("Calculate the area of triangle")
            base = float(input("Enter the bias: "))
            height = float(input("Enter the area of height: "))
            area = triangle_area(base, height)
            print(area)
        
        elif choice == 3:
            print("Calculate the Area of Circle and Triangle: ")
            radius  = float(input("Enter the radius: ")) 
            base = float(input("Enter the bias: "))
            height = float(input("Enter the area of height: "))
            area1 = circle_area(radius)
            area2 = triangle_area(base, height)
            print(f"The area of both: Circle: {area1:.2f}, Triangle: {area2:.2f}")
    except ValueError:
        print("Invalid input, try again")
if __name__ == "__main__":
    main()

print("####################################################")

# finding Area of Circle and Triangle

pie = 3.1416

radius = float(input('Enter the radius: '))

circle = pie * radius ** 2

base = float(input("Enter the input of base: "))
height = float(input("Enter the input of height: "))
triangle = 0.5 * base * height

print(f"The result of {circle} and {triangle}")


print("####################################################")