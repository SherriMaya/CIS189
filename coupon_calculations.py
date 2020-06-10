def calculate_order(price, cash_coupon, percent_coupon):
    ship = 0

    dis_price = (price - cash_coupon) * ((100-percent_coupon)/100)
    after_tax = dis_price *1.06

    if dis_price < 10:
        ship = 5.95
    elif 10 < dis_price < 30:
        ship = 7.95
    elif 30 < dis_price < 50:
        ship = 11.95
    else:
        ship = 0

    total = after_tax + ship
    print("%.2f" % total)

calculate_order(15.99,5,30)