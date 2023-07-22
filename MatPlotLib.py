# QAP 4: Sales Plotting
# Program Description: A program to graph monthly sales
# Written By: Vanessa Rice
# Written On: July 18, 2023

import matplotlib.pyplot as plt

def get_monthly_sales():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales = []

    for month in months:
        try:
            sales_amount = float(input(f"Enter the total sales amount for {month}: $"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return get_monthly_sales()

        sales.append(sales_amount)

    return months, sales

def plot_sales_graph(months, sales):
    plt.figure(figsize=(10, 6))
    plt.plot(months, sales, marker='o', color='b', label='Total Sales')
    plt.xlabel('Months')
    plt.ylabel('Total Sales ($)')
    plt.title('Monthly Total Sales')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    print("Please enter the total sales for each month:")
    months, sales = get_monthly_sales()
    plot_sales_graph(months, sales)

if __name__ == "__main__":
    main()
