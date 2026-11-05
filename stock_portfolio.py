# CodeAlpha Python Internship
# Task 2: Stock Portfolio Tracker

import json
import os

# Sample stock prices (in INR)
stocks = {
    "TCS": 3500,
    "INFOSYS": 1800,
    "WIPRO": 500,
    "RELIANCE": 2900,
    "HDFC": 1700,
    "ICICI": 1200,
    "ITC": 450,
    "TATA MOTORS": 800
}

portfolio = {}
FILE_NAME = "portfolio.json"


# Display available stocks
def display_stocks():
    print("\n========== AVAILABLE STOCKS ==========")

    for name, price in stocks.items():
        print(f"{name:<15} Rs.{price}")

    print("======================================")


# Buy stocks
def buy_stock():
    display_stocks()

    name = input("\nEnter stock name: ").strip().upper()

    if name not in stocks:
        print("Stock not available!")
        return

    try:
        quantity = int(input("Enter quantity to buy: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        portfolio[name] = portfolio.get(name, 0) + quantity

        print(f"\nSuccessfully purchased {quantity} shares of {name}!")

        save_portfolio()

    except ValueError:
        print("Please enter a valid whole number.")


# Sell stocks
def sell_stock():
    if not portfolio:
        print("\nYour portfolio is empty!")
        return

    view_holdings()

    name = input("\nEnter stock name to sell: ").strip().upper()

    if name not in portfolio:
        print("You do not own this stock!")
        return

    try:
        quantity = int(input("Enter quantity to sell: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")

        elif quantity > portfolio[name]:
            print("You do not have enough shares!")

        else:
            portfolio[name] -= quantity

            if portfolio[name] == 0:
                del portfolio[name]

            print(f"\nSuccessfully sold {quantity} shares of {name}!")

            save_portfolio()

    except ValueError:
        print("Please enter a valid whole number.")


# Display stock holdings
def view_holdings():
    print("\n========== YOUR STOCK HOLDINGS ==========")

    if not portfolio:
        print("Your portfolio is empty!")
        return

    for name, quantity in portfolio.items():
        print(f"{name} : {quantity} shares")

    print("==========================================")


# Calculate portfolio value
def calculate_portfolio():
    if not portfolio:
        print("\nYour portfolio is empty!")
        return

    total_value = 0

    print("\n========== PORTFOLIO SUMMARY ==========")

    print(f"{'Stock':<15}{'Quantity':<12}{'Price':<12}{'Value'}")

    print("-" * 55)

    for name, quantity in portfolio.items():

        price = stocks[name]
        value = price * quantity

        total_value += value

        print(
            f"{name:<15}{quantity:<12}"
            f"Rs.{price:<9}Rs.{value}"
        )

    print("-" * 55)

    print(f"Total Portfolio Value: Rs.{total_value}")

    print("=======================================")


# Save portfolio to JSON file
def save_portfolio():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(portfolio, file, indent=4)

        print("\nPortfolio saved successfully!")

    except OSError:
        print("Error saving portfolio!")


# Load previously saved portfolio
def load_portfolio():
    global portfolio

    if os.path.exists(FILE_NAME):

        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("Invalid portfolio format")

            for name, quantity in data.items():
                if (
                    name not in stocks
                    or type(quantity) is not int
                    or quantity <= 0
                ):
                    raise ValueError("Invalid portfolio data")

            portfolio = data

            print("Previous portfolio loaded successfully!")

        except (OSError, json.JSONDecodeError, ValueError):
            portfolio = {}
            print("Could not load saved portfolio. Starting a new one.")


# Main menu
def main():

    load_portfolio()

    while True:

        print("\n======================================")
        print("       STOCK PORTFOLIO TRACKER")
        print("======================================")

        print("1. Display Available Stocks")
        print("2. Buy Stocks")
        print("3. Sell Stocks")
        print("4. View Stock Holdings")
        print("5. Calculate Portfolio Value")
        print("6. Save Portfolio")
        print("7. Exit")

        print("======================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_stocks()

        elif choice == "2":
            buy_stock()

        elif choice == "3":
            sell_stock()

        elif choice == "4":
            view_holdings()

        elif choice == "5":
            calculate_portfolio()

        elif choice == "6":
            save_portfolio()

        elif choice == "7":
            save_portfolio()
            print("\nThank you for using Stock Portfolio Tracker!")
            break

        else:
            print("\nInvalid choice! Please select 1 to 7.")


# Run the application
if __name__ == "__main__":
    main()