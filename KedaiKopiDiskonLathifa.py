class Menu:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class Diskon:
    def __init__(self):
        self.__diskon_rate = {
            1: 0.0,
            2: 0.1,
            3: 0.15,
            4: 0.2,
            5: 0.25
        }

    def get_diskon_rate(self, quantity):
        if quantity >= 5:
            return self.__diskon_rate[5]
        elif quantity >= 4:
            return self.__diskon_rate[4]
        elif quantity >= 3:
            return self.__diskon_rate[3]
        elif quantity >= 2:
            return self.__diskon_rate[2]
        else:
            return self.__diskon_rate[1]

class CoffeeShop:
    def __init__(self):
        self.__menu = {
            "a": Menu("ES Kopi Susu", 11000),
            "b": Menu("ES Kopi Coklat", 12000),
            "c": Menu("ES Kopi Hitam", 11000),
            "d": Menu("Ice Americano", 14000),
        }
        self.__ppn_rate = 0.1
        self.__diskon = Diskon()


    def __calculate_discount(self, total_price, quantity):
        diskon_rate = self.__diskon.get_diskon_rate(quantity)
        return int(total_price * diskon_rate)

    def __calculate_ppn(self, total_price):
        return int(total_price * self.__ppn_rate)

    def calculate_total_price(self, choice, quantity):
        if choice not in self.__menu:
            return None

        menu = self.__menu[choice]
        total_price = menu.get_price() * quantity
        discount = self.__calculate_discount(total_price, quantity)
        ppn = self.__calculate_ppn(total_price - discount)
        total_price_with_ppn_and_discount = total_price - discount + ppn

        return {
            "menu": menu.get_name(),
            "quantity": quantity,
            "price": total_price,
            "discount": discount,
            "ppn": ppn,
            "total_price": total_price_with_ppn_and_discount,
        }


class Customer:
    def __init__(self, coffee_shop):
        self.__coffee_shop = coffee_shop

    def order(self, choice, quantity):
        result = self.__coffee_shop.calculate_total_price(choice, quantity)
        if result is None:
            return None

        return result

coffee_shop = CoffeeShop()
customer = Customer(coffee_shop)

while True:
    print("""
    ==============================
    
    Ananda Coffe
    List Menu Minuman Kopi
 
    ==============================
    A. ES Kopi Susu : Rp 11.000
    B. ES Kopi Coklat : Rp 12.000
    C. ES Kopi Hitam : Rp 11.000
    D. Ice Americano : Rp 14.000
    ==============================
    """)
    choice = input("Masukkan list abjad menu kopi = ").lower()
    quantity = int(input("Masukkan jumlah pesanan = "))

    result = customer.order(choice, quantity)
    if result is None:
        print("Menu tidak tersedia, silakan masukkan abjad menu yang tersedia.")
    else:
        print("--------------------------")
        print("Ananda Coffee")
        print("--------------------------")
        print("Menu :", result["menu"])
        print("Jumlah Pesan :", result["quantity"])
        print("Harga :", result["price"])
        print("Diskon :", result["discount"])
        print("PPN :", result["ppn"])
        print("--------------------------")
        print("Jumlah Bayar :", result["total_price"])
        print("--------------------------")

    choice = input("Apakah Anda ingin order kembali (Y/N) = ").lower()
    if choice != "y":
        break