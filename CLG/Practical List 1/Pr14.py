#  Write a Python program to find profit or loss based on cost price and sell price
# of an item. Also print profit or loss percentage. (Profit and loss must be
# positive number only)

def main():
    # Get user input for cost price and sell price
    cost_price = float(input("Enter the cost price: "))
    sell_price = float(input("Enter the sell price: "))

    # Calculate profit or loss
    p_l = sell_price - cost_price

    # Calculate profit or loss percentage (using absolute value to ensure it's positive)
    profit_or_loss_percentage = abs((p_l / cost_price) * 100)

    # Determine if it's a profit, loss, or break-even
    if p_l > 0:
        status = "Profit"
    elif p_l < 0:
        status = "Loss"
    else:
        status = "No Profit No Loss"

    # Display the result using str for concatenation
    print("Result: " + status + ", " + str(abs(p_l)) + " Rs/-")
    print("Percentage: " + str(profit_or_loss_percentage) + "%")

# Call the main function
main()
