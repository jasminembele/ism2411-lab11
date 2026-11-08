# Customers.py
# Jasmine Mbele
# Self Reflection:
# 1. I would use .get() in the real world when reading user submitted data from a form. This is because the user may not fill out all the fields, and using .get() allows me to provide a default value instead of raising an error. I would use bracket notation when processing data that I know will always be present, such as required fields in a database record. This is because bracket notation is more straightforward and can be more efficient when I am certain that the key exists.
print("--- Exercise 1 ---")
customer = {
    "name": "Alice", # Key: Value,
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])


print("--- Exercise 2 ---")
customer['phone'] = '555-5555' # Adding a new key-value pair to the dictionary
print(customer)
customer['tier'] = 'platinum' # Updating the value of an existing key
print(customer)
del customer['name'] # Deleting a key-value pair from the dictionary
print(customer)

print(customer.get('ytd_spend', 0)) # Using the get() method to retrieve a value with a default message if the key doesn't exist


print("--- Exercise 3 ---")
print(customer.get("email", "no email on file")) # Using the get() method to retrieve a value with a default message if the key doesn't exist

# try:
#    print(customer["email"]) # This will raise a KeyError because the key is misspelled
# except KeyError as error:
#    print("KeyError caught:", error) # Catching the KeyError and printing an error message


print("--- Exercise 4 ---")
for key, value in customer.items(): # Iterating over the dictionary and printing each key-value pair
    print(f"{key}: {value}") # Iterating over the dictionary and printing each key-value pair

for key in customer:
    print(key, customer[key]) # Iterating over the dictionary and printing each key-value pair


print("--- Exercise 5 ---")
tier_discounts = {
    "bronze": 0, 
    "silver": 0.05, 
    "gold": 0.1, 
    "platinum": 0.15 
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0) # Using the get() method to retrieve a value with a default message if the key doesn't exist
final_price = purchase * (1 - discount_rate) # Calculating the final price after applying the discount
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")


print("--- Exercise 6 ---")

customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0) # Using the get() method to retrieve a value with a default message if the key doesn't exist
    discount = 300 * rate # Calculating the discount based on the tier
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase") # Printing the discount for each customer


print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details['stock']} left") # Printing a warning message for items with low stock


print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount # Using the get() method to retrieve a value with a default message if the key doesn't exist
print(sales_by_region) # Printing the total sales by region

for region in sorted(sales_by_region): # Sorting the regions alphabetically and printing the total sales for each region
    print(f"{region}: ${sales_by_region[region]:.2f}")