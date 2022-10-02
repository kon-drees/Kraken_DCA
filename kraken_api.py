import time
import requests
import urllib.parse
import hashlib
import hmac
import base64
import order
from logger import Logger


class KrakenApi:

    def __init__(self, logger: Logger, api_key='', api_sec=''):
        self.api_key = api_key
        self.api_sec = api_sec
        self.api_url = "https://api.kraken.com"
        self.logger = logger

    def load_keys(self):
        with open("./api_keys.key", 'r') as f:
            self.api_key = f.readline().strip()
            self.api_sec = f.readline().strip()
        return

    def get_kraken_signature(self, urlpath, data):
        postdata = urllib.parse.urlencode(data)
        encoded = (str(data['nonce']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()

        mac = hmac.new(base64.b64decode(self.api_sec), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()

    # Attaches auth headers and returns results of a POST request
    def kraken_request(self, uri_path, data):
        headers = {}
        headers['API-Key'] = self.api_key
        headers['API-Sign'] = self.get_kraken_signature(uri_path, data)
        req = requests.post((self.api_url + uri_path), headers=headers, data=data)
        return req

    # Places an order and returns results of a Post requests
    def kraken_place_order(self, kraken_order: order.Order):

        # market order where volume is base currency
        if kraken_order.order_type == "market":
            resp = self.kraken_request('/0/private/AddOrder', {
                "nonce": str(int(1000 * time.time())),
                "ordertype": kraken_order.order_type,
                "type": kraken_order.order_direction,
                "volume": kraken_order.order_volume,
                "pair": kraken_order.order_pair,
                "oflags": "viqc"

            })
            self.logger.log(resp.text)
            return resp

        # limit order
        elif kraken_order.order_type == "limit":
            resp = self.kraken_request('/0/private/AddOrder', {
                "nonce": str(int(1000 * time.time())),
                "ordertype": kraken_order.order_type,
                "type": kraken_order.order_direction,
                "volume": kraken_order.order_volume,
                "pair": kraken_order.order_pair,
                "price": kraken_order.order_price
            })
            self.logger.log(resp.text)
            return resp

        else:
            self.logger.log("Invalid order type")
