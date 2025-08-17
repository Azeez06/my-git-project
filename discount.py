def calculate_discount():
    price = int(input("Enter a price: "))
    discount_percent = int(input("Enter a discount percent: "))
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        print("Final Price after discount:", final_price)
    else:
        print("No discount applied. Price remains:", price)

calculate_discount()
