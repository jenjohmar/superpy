# Imports
import argparse
from helpers import *

# 1. opens bought.csv looks at current total line count
# 2. increments total line count with 1 = id
# 3. creates new dict from data passed in and adds the id
# 4. writes dict to bought.csv
# 5. if amount > 1 each product gets own line and unique id

def buy(prod_name: str, buy_price: float, buy_date: str, exp_date: str, amount: int):
    
    number_of_lines = 0

    create_csv("bought.csv", header_bought)

    with open('bought.csv', 'r') as csv_file:
        for line in csv_file:
            number_of_lines += 1

    id = number_of_lines

    new_product_dict = {
        "product_id": id,
        "product_name": prod_name,
        "buy_price": buy_price,
        "buy_date": buy_date,
        "exp_date": exp_date,
        }
    for i in range(amount):
        old_id = new_product_dict["product_id"]
        new_id = old_id + 1
        new_product_dict["product_id"] = new_id
        write_to_bought(new_product_dict)
    print(f"Product bought successfully!")

parser = argparse.ArgumentParser(description="Buy product(s).")
            
parser.add_argument("prod_name", help="Enter product name in lowercase (i.e. 'orange').")
parser.add_argument("buy_price", type=float, help="Enter product buy price (format 0.00).")
parser.add_argument("buy_date", help="Enter product buy date (format: yyyy-m-d).")
parser.add_argument("exp_date", help="Enter product expiration date (format: yyyy-m-d).")
parser.add_argument("amount", type=int, help="Enter amount (number) of products to buy.")

args = parser.parse_args()

buy(prod_name=args.prod_name, buy_price=args.buy_price, buy_date=args.buy_date, exp_date=args.exp_date, amount=args.amount)


        
    