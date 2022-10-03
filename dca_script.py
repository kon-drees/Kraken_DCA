import json
from typing import List

from kraken_api import KrakenApi
from logger import Logger
from order import Order
from pathlib import Path


def read_orders_from_file(logger: Logger) -> List[Order]:
    orders_file = Path("orders.json")
    orders_file_content = orders_file.open("r").read()
    orders_json = json.loads(orders_file_content)
    orders = []
    for kraken_order in orders_json:
        orders.append(Order(order_pair=kraken_order["pair"],
                            order_direction=kraken_order["direction"],
                            order_type=kraken_order["type"],
                            order_volume=kraken_order["volume"]))

    return orders


if __name__ == '__main__':
    logger = Logger("./log.txt")
    orders = read_orders_from_file(logger)
    kraken = KrakenApi(logger)
    kraken.load_keys()
    for order in orders:
        kraken.kraken_place_order(order)



