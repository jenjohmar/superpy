import argparse
from helpers import *

# 1. opens sold.csv looks at current total line count
# 2. increments total line count with 1 = id
# 3. creates new dict from data passed in, adds id + finds bought_id and adds that
# 4. writes dict to sold.csv
# 5. if amount > 1 each product gets own line and unique sold_id

def sell(prod_name: str, sell_date: str, sell_price, amount):
    create_csv("sold.csv", header_sold)
    
    number_of_lines = 0
    with open('sold.csv', 'r') as csv_file:
        for line in csv_file:
            number_of_lines += 1

    id = number_of_lines
 
    new_product_dict = {
        "product_id": id,
        "bought_id": 0,
        "product_name": prod_name,
        "sell_date": sell_date,
        "sell_price": sell_price,
    }

    # 1. checks inventory if product given is in inventory (and stores how many times), if True: 
    # 2. makes sure product id is incremented by 1 for each row so each product has unique sold id
    # 3. searches bought_id for each product and adds that to each product
    # 4. calls write_to_sold, row created for each unique product
    inventory = check_inventory(sell_date, prod_name)

    found = False
    count = 0

    for list_item in inventory:
        if prod_name in list_item:
            count += 1
            found = True
    if found == True:
        if amount <= count:
            for number in range(amount):
                old_id = new_product_dict["product_id"]
                new_id = old_id + 1
                new_product_dict["product_id"] = new_id

                bought_id = find_product_id(prod_name, "bought.csv", (number + 1))

                new_product_dict["bought_id"] = bought_id

                write_to_sold(new_product_dict)
            print(f"Product sold succesfully!")
        else:
            print(f"Amount exceeds product count in inventory! You can currently sell {count} of {prod_name}.")

    else:
        print(f"Product {prod_name} not in inventory!")
                 
parser = argparse.ArgumentParser(description="Sell product(s).")
            
parser.add_argument("prod_name", help="Enter product name in lowercase (i.e. 'orange').")
parser.add_argument("sell_date", help="Enter product sell date (format: yyyy-m-d).")
parser.add_argument("sell_price", help="Enter product sell price (format: yyyy-m-d).")
parser.add_argument("amount", type=int, help="Enter amount (number) to sell.")

args = parser.parse_args()

sell(prod_name=args.prod_name, sell_date=args.sell_date, sell_price=args.sell_price, amount=args.amount)