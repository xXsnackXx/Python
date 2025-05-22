#IMPORT--------------------------
import random
#IMPORT--------------------------



# Constant varibles---------------
MAX_LINES = 3
MAX_BET = 100     # Can change to update program
MIN_BET = 1
ROW = 3
COL = 3
# Constant varibles---------------

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [[], [], []]
    for col in range(rows):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for column in columns:
            print(column[row], "|")
        

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
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")#f with curly brakets inputs var into string
        else:
            print("Please enter a number.")
    return amount

# Main program loop calls 
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. your current balance is: ${balance}")
        else:
            break
        
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")



main()

