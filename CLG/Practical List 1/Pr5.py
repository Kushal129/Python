def main():
    # Define variable values
    x = 2
    y = 3
    z = 5
    a = 4
    b = 5

    # Evaluate each equation using the defined variable values
    equation1 = x + y * z
    equation2 = x * y + a * b**2
    equation3 = a**2 + 2 * a * b + b**2
    equation4 = a**2 - 2 * a * b + b**2
    equation5 = (a - b) * (a + b)
    equation6 = a**3 + b**3 + 3 * a * b * (a + b)
    equation7 = a**3 - b**3 - 3 * a * b * (a - b)
    equation8 = (a - b) * (a**2 + a * b + b**2)
    equation9 = (a + b) * (a**2 - a * b + b**2)
    equation10 = 3 * x * y**3 + 9 * x**2 * y**3 + 5 * y**3 * x

    # Print the results
    print("Equation 1:", equation1)
    print("Equation 2:", equation2)
    print("Equation 3:", equation3)
    print("Equation 4:", equation4)
    print("Equation 5:", equation5)
    print("Equation 6:", equation6)
    print("Equation 7:", equation7)
    print("Equation 8:", equation8)
    print("Equation 9:", equation9)
    print("Equation 10:", equation10)

# Call the main function
main()