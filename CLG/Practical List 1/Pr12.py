# Write a Python program to find volume of sphere. Formula V=(4πr^3)/3
# where π=3.14 and r is radius of sphere.
import math
def sphere_vol(radius):
    return (4 * math.pi * radius**3) / 3

def main():
    # Get user input for the radius of the sphere
    radius = float(input("Enter the radius of the sphere: "))

    # Calculate the volume of the sphere using the formula
    volume = sphere_vol(radius)

    # Display the result
    print("The volume of the sphere with radius " + str(radius) + " is " + str(volume) + " cubic units.")

# Call the main function
main()
