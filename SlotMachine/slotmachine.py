# Constant varibles---------------
MAX_LINES = 3
MAX_BET = 100     # Can change to update program
MIN_BET = 1
# Constant varibles---------------


# User geting deposit function
def deposit():
    while True:
        amount = input("What would you like to deposit $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

# User geting line bet function
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Amount must be 1, 2, or 3.")
        else:
            print("Please enter a number.")
    return lines

# User geting bet function
def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")#f with curly brakets inputs var into string
        else:
            print("Please enter a number.")

# Main program loop calls 
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()

