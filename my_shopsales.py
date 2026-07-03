# Expand on the products, create 3 products using this template
# Day 1 milk 2 units ,water 2 units each, such progress price, what has been sold, the amount made and what is left

# Day 2 bread was sold 3 units, water was sold 1 unit
# Day 3 each item was sold for 4 units
# water having the least amount of supply has 10 units, and bread has double the figures and milk has double what bread has
# add extra field at my own discretion 

# Create 3 products
# Starting inventory
milk = {"name": "milk", "selling_price": 2.20, "quantity": 80, "expiry_date": "2025/03/11"}

bread = {"name": "bread", "selling_price": 3.50, "quantity": 40, "expiry_date": "2025/02/15"}

water = {"name": "water", "selling_price": 1.00, "quantity": 10, "expiry_date": "2026/01/01"}


# DAY 1

milk_sold = 2
water_sold = 2

milk_revenue = milk_sold * milk["selling_price"]
water_revenue = water_sold * water["selling_price"]

milk["quantity"] = milk["quantity"] - milk_sold
water["quantity"] = water["quantity"] - water_sold

day1_total = milk_revenue + water_revenue
# print("Sold:", milk_sold, "milk,", water_sold, "water")
print(day1_total)

# DAY 2

bread_sold = 3
water_sold = 1

bread_revenue = bread_sold * bread["selling_price"]
water_revenue = water_sold * water["selling_price"]

bread["quantity"] = bread["quantity"] - bread_sold
water["quantity"] = water["quantity"] - water_sold

day2_total = bread_revenue + water_revenue
print("Sold:", bread_sold, "bread,", water_sold, "water")
print(day2_total)

# DAY 3

milk_sold = 4
bread_sold = 4
water_sold = 4

milk_revenue = milk_sold * milk["selling_price"]
bread_revenue = bread_sold * bread["selling_price"]
water_revenue = water_sold * water["selling_price"]

milk["quantity"] = milk["quantity"] - milk_sold
bread["quantity"] = bread["quantity"] - bread_sold
water["quantity"] = water["quantity"] - water_sold

day3_total = milk_revenue + bread_revenue + water_revenue
print("Sold:", milk_sold, "milk,", bread_sold, "bread,", water_sold, "water")
print(day3_total)

# FINAL SALES FOR THE 3 DAYS

print("Milk remaining:", milk["quantity"], "units")
print("Bread remaining:", bread["quantity"], "units")
print("Water remaining:", water["quantity"], "units")

total_revenue = day1_total + day2_total + day3_total
print(total_revenue)