# CODEALPHA INTERNSHIP TASK#02:  "STOCK PORTFOLIO TRACKER"

stock_prices = {
    "TSLA" : 411.82,
    "MSFT" : 397.23,
    "GOOGL" : 314.98,
    "AAPL" : 264.58,
    "AMZN" : 210.11,
    "NVDA" : 189.82
}

portfolio_data = []

print("\n========== WELCOME TO STOCK PORTFOLIO TRACKER ==========\n")

print("Currently Available Stocks (with their names and price per share):")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\n• Please enter the stock details below.")
print("• You can add stocks one by one.")
print("• Type 'no' when you are done to view your full portfolio.\n")

while True:
    stock_name = input("Enter stock name: ").upper().strip()

    if stock_name in stock_prices:
        try:
            quantity = float(input("Enter quantity: "))
            if quantity <= 0:
                print("Please enter a valid positive number.\n")
                continue
        except ValueError:
            print("Please enter a valid positive number.\n")
            continue

        total_investment_value = stock_prices[stock_name] * quantity
        print(f"Total Investment Value: ${total_investment_value:.2f}")

        portfolio_data.append({
            "stock": stock_name,
            "price": stock_prices[stock_name],
            "quantity": quantity,
            "total": total_investment_value
        })

        with open("stock_tracker_file.txt", "a") as portfolio:
            portfolio.write(f"Stock: {stock_name}\n")
            portfolio.write(f"Price per share: ${stock_prices[stock_name]:.2f}\n")
            portfolio.write(f"Quantity: {quantity}\n")
            portfolio.write(f"Total Investment: ${total_investment_value:.2f}\n")
            portfolio.write("--------------------------\n")
    else:
        print("Stock not found.")
        
    choice = input("\nDo you want to add another stock? (yes/no): ").lower()
    if choice != "yes":

        if portfolio_data:
            print("\n------ Your Portfolio ------")

            overall_total = 0

            for item in portfolio_data:
                print(f"Stock: {item['stock']}")
                print(f"Price per share: ${item['price']:.2f}")
                print(f"Quantity: {item['quantity']}")
                print(f"Total Investment: ${item['total']:.2f}")
                print("----------------------------")

                overall_total += item['total']

            print(f"\n*** Total Portfolio Value: ${overall_total:.2f} ***\n")

        else:
            print("\nNo stocks were added to your portfolio.")

        break
