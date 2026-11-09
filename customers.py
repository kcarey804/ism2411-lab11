# 1. I would use .get() when I am not sure if a key exists because it gives me a default value instead of causing an error. I would use bracket notation when I know the key exists and need its value. My rule of thumb is to use .get() for safer lookups and brackets when I know the information is there. 
# 2. The summary dictionary in Exercise 8 reminds me of using SUMIF in Excel because it adds together values that belong to the same category. Python can be more useful for large datasets because it can automatically process lots of information using loops without having to manually create formulas for each category. 

# Exercise 1
customer = {
  "name": "Kaitlyn",
  "email": "kaitlyn@email.com",
  "tier": "Gold",
  "ytd_spend": 1250
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2
customer["phone"] = "555-123-4567"
print(customer)

del customer["email"]
print(customer)

#Exercise 3
print(customer.get("email", "no email on file"))

print(customer["email"])

# Exercise 4
for key, value in customer.items():
  print(f"{key}: {value}")

for key in customer:
  print(key)

# Exercise 5
tier_discounts = {
  "bronze": 0,
  "silver": .05,
  "gold": .10,
  "platinum": .15
}

tier = customer["tier"]
discount = tier_discounts.get(tier,0)

purchase_price = 200
final_price = purchase_price * (1 - discount)

print("Tier:", tier)
print("Discount rate:", discount)
print("Final price:", final_price)

#Exercise 6
customers = [
  {"name": "Sarah", "tier": "platinum"},
  {"name": "John", "tier": "gold"},
  {"name": "Emily", "tier": "silver"}

for customer in customers:
  tier = customer["tier"]
  discount = tier_discounts.get(tier,0)
  final_price = 300 * (1 - discount)

  print("Name:", customer["naame])
  print("Tier:", tier)
  print("Discount:", discount)
  print("Final price:", final_price)
  print()

#Exercise 7
catalog = {
  "Widget A": {"price": 9.99, "stock":150},
  "Gadget C": {"price": 49.99, "stock": 8}

for product, details in catalog.items():
  if details["stock"] < 20:
    print("LOW STOCK:", product)

#Exercise 8
transactions = [ 
  {"region": "North", "amount": 100}
  {"region": "South", "amount": 200}
  {"region": "North", "amount": 150}
  {"region": "East", "amount": 300}
  {"region": "South", "amount": 50}
]

sales_summary = {}

for transaction in transactions:
  region = transaction["region"]
  amount = transaction["amount"]

  sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
  print(region, ":", sales_summary[region])
