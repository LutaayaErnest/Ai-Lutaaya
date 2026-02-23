# Hard-coded price
price = 6700

# Assume customer pays 10000 shillings
paid = 10000

# Calculate change
change = paid - price

# Calculate number of each coin using integer division and modulus
coin1000 = change // 1000
change = change % 1000

coin500 = change // 500
change = change % 500

coin200 = change // 200
change = change % 200

coin100 = change // 100
change = change % 100

# Output
print("The price of your item is", price, "shillings, and your change is", paid - price, "shillings.")
print("Here's the change that uses the fewest coins:\n")

print("1000 shillings:", coin1000)
print("500 shillings:", coin500)
print("200 shillings:", coin200)
print("100 shillings:", coin100)