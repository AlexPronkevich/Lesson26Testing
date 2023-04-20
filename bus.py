# private
# public
# protected


class Bus:
    def __init__(self, brand='no name', price=0, number=0):
        self._brand = brand        # protected
        self._price = price        # protected
        self._number = number      # protected


    # def __del__(self):
    #     print(f"destructor for {self.brand}")


    def __str__(self):
        return f"Bus: {self._brand}, price = ${self._price}, number = {self._number}"


if __name__ == "__main__":
    bus = Bus()
    bus.number = -10    # protected
    print(bus)

