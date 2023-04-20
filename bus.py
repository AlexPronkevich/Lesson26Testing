# private
# public
# protected


class Bus:
    def __init__(self, brand='no name', price=0, number=0):
        self.brand = brand        # public
        self.price = price        # public
        self.number = number      # public


    # def __del__(self):
    #     print(f"destructor for {self.brand}")


    def __str__(self):
        return f"Bus: {self.brand}, price = ${self.price}, number = {self.number}"


if __name__ == "__main__":
    bus = Bus()
    bus.number = -10    # public

