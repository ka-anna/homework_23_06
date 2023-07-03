#Write a function called calculate_area that takes the radius of a circle as an argument. Inside the function,
#calculate the area of the circle (πr^2) and print it. Test the function by calling it with different radius values.


def calculate_area(radius):
    area = 2*3.14*radius
    return area

res = calculate_area(6)
print(res)
