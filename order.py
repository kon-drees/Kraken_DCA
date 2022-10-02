class Order:
    def __init__(self, order_pair: str,
                 order_volume: float,
                 order_direction: str,
                 order_type: str,
                 order_price: float = 0.0
                 ):
        self.order_pair = order_pair
        self.order_volume = order_volume
        self.order_direction = order_direction
        self.order_type = order_type
        self.order_price = order_price

    def __str__(self):
        return f"{self.order_direction}, {self.order_pair}, volume: {self.order_volume}"
