# private
# public
# protected


class Bus:
    def __init__(self, brand='no name', price=0, number=0):
        self.__brand = brand        # private
        self.__price = price        # private
        self.__number = number      # private


    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.price = price


    # def __del__(self):
    #     print(f"destructor for {self.brand}")


    def __str__(self):
        return f"Bus: {self.__brand}, price = ${self.__price}, number = {self.__number}"


if __name__ == "__main__":
    bus = Bus()
    print(bus.__numder)

