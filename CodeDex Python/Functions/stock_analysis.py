#stock_analysis.py

# Create functions that get the highest price/lowest price/or price on certain date of AMC stock

stock_prices = [ 6.15, 5.81, 5.70, 5.65, 5.33, 5.62, 5.19, 6.13, 7.20, 7.34, 7.95, 7.53, 7.39, 7.59, 7.27 ]


def max_price(a, b):
    return max(stock_prices[(a - 1):b])

def min_price(a,b):
    return min(stock_prices[(a - 1):b])

def price_at(x):
    return stock_prices[x - 1]

while(True):
    print('This program currently contains value of AMC Stock between 11/1/2022 to 11/21/2022')
    print('Available prices only include days the market was open')
    print('Pick a function that you would like to perform:')
    print('  1) Find the max price of AMC Stock between two dates')
    print('  2) Find the minimum price of AMC Stock between two dates')
    print('  3) Find the price of AMC Stock on a certain date')
    print('  4) Exit the application')

    choice = int(input('Please select an option(1-4): '))
    
    if choice == 1:
        print('Please select the first date you would like between 11/1/2022 - 11/21/2022.')
        a = int(input('The dates are enumerated between 1-15: '))
        print('Please select the second date you would like between 11/1/2022 - 11/21/2022.')
        b = int(input('The dates are enumerated between 1-15: '))
        print(f'The Highest price for AMC stock between those dates is {max_price(a, b)}')
    
    elif choice == 2:
        print('Please select the first date you would like between 11/1/2022 - 11/21/2022.')
        a = int(input('The dates are enumerated between 1-15: '))
        print('Please select the second date you would like between 11/1/2022 - 11/21/2022.')
        b = int(input('The dates are enumerated between 1-15: '))
        print(f'The Lowest price for AMC stock between those dates is {min_price(a, b)}')

    elif choice == 3:
        print('Please select the date you would like to know the price of between 11/1/2022 - 11/21/2022.')
        x = int(input('The dates are enumerated between 1-15: '))
        
        print(f'The price for AMC stock on that dates is {price_at(x)}')

    else:
        print('Thank you for using my application')
        break