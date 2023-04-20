from bus import Bus


class Manager:


    def find_bus(buses):
        if not isinstance(buses, (list, tuple)):
            return Bus()

        target = buses[0]

        for bus in buses:
            if isinstance(bus, Bus):
                if (bus.__price / bus.__number) < (target.__price / target.__number):
                    target = bus

        return target
