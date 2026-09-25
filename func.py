def calculate_member_discount(price, member_type):
    # member_discount = price - (price * member_type / 100)
    
    if member_type == "GOLD":
        net_price = price - (price * 15 / 100)
    elif member_type == "SILVER":
        net_price = price - (price * 10 / 100)
    elif member_type == "NORMAL":
        net_price = price - (price * 0 / 100)
    else:
        exit()
    return net_price

def process_coffee_order(drink_name, price, member_type):
   
    final_price = calculate_member_discount(price, member_type)

    print(f"สินค้า : {drink_name} | ราคาขายจริงหลังลด {member_type}% คือ : {final_price:.2f} บาท")

process_coffee_order("กาแฟ", 100, "GOLD")