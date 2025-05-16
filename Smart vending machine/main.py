# Make item list.
# Make a function to accept user's input(item by code, code by price)
# Make a function to take transaction (loop for transactions until exit)

product = [
    {
        "console": "XBOx",
        "code": "A1",
        "price": 100
    },
    {
        "console": "PS1",
        "code": "A2",
        "price": 200
    },
    {
        "console": "PS2",
        "code": "A3",
        "price": 300
    },
    {
        "console": "PS3",
        "code": "A4",
        "price": 400
    },
    {
        "console": "PS4",
        "code": "A5",
        "price": 500
    }
]

def counter(items):
    cash = int(input("Deposit(10 - 100): "))
    balance = cash
    
    while balance < 100:
        cash = int(input("The minimum deposit is 10, please try again: "))
        balance = cash
        print("Your balance is: ", balance)

    transaction_code = input("Purchase an item by entering the code: ")
    
    for item in items:
        if transaction_code == item["code"] and balance > 100:
            remaining_balance = balance - item["price"]
            print("You bought a ",item["console"],".Your remaining balance is", remaining_balance)
        
       
counter(product)