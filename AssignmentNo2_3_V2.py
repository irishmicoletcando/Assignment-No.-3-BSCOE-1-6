# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def ask_money():
    _money = float(input("How much money do you have? "))
    return _money

def ask_price_apple():
    _apple = float(input("What is the price of an apple per piece? "))
    return _apple

def max_number_apples():
    max_number_apples = int(money // apple)
    return max_number_apples

def show_change():
    _change = money % apple
    return _change

def display():
    print(f"You can buy {maximum_apples} apples and your change is {change: .2f} pesos.")


money = ask_money()
apple = ask_price_apple()
maximum_apples = max_number_apples()
change = show_change()
display()

# Program completed