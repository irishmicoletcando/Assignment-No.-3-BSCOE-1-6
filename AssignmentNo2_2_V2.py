# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def ask_apples_number_to_compute_price():
    apple_number = int(input("How many apples do you want to buy? "))
    apple_price = 20 * apple_number
    return apple_price

def ask_oranges_number_to_compute_price():
    orange_number = int(input("How many oranges do you want to buy? "))
    orange_price = 25 * orange_number
    return orange_price

def show_total(apple, orange):
    apple_and_orange_total = apple + orange
    return apple_and_orange_total

def display(totalamount):
    print(f"The total amount is {totalamount}.")


apple = ask_apples_number_to_compute_price()
orange = ask_oranges_number_to_compute_price()
total = show_total(apple, orange)
display(total)

# Program Completed