# Customers.py
# Jasmine Mbele

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