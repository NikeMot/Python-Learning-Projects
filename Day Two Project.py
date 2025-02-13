#Program which allows to calculate salespeople's commissions

name = input("Please, enter your name:\n")
surname = input("Please, enter your surname\n")
sales = float(input("Now, please enter your total sales value for this month:\n£ "))

commission = round(sales*0.13, 2)

print(f"Hello, {name} {surname}. Your monthly commission amounts to £{commission}")
