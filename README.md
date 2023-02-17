# Kraken Dollar-Cost-Averaging Script
 Simple [Kraken](https://www.kraken.com/) DCA Script using the Kraken API


# Instructions
[Generate](https://www.kraken.com/u/security/api) your Kraken key and enter it in the api_keys.key file. 
Enter your Orders in the orders.json file. For example:

```json
[
  {
    "pair": "XETHZEUR",
    "direction": "buy",
    "type": "market",
    "volume": 20
  },
  {
    "pair": "XXBTZEUR",
    "direction": "buy",
    "type": "market",
    "volume": 20
  },
  {
    "pair": "ALGOEUR",
    "direction": "buy",
    "type": "market",
    "volume": 10
  }
]
```

Start the script from the folder via console command:

```cmd
python3 dca_script.py    
```

The script writes all executed orders or any exceptions in the log file.

You can use the script with an automator Tool and specify at which date the orders should be executed.

# Order json Explanation

pair: Trading Asset Pairs from [Kraken](https://support.kraken.com/hc/en-us/articles/201893658) 

direction: "buy" or "sell"

type: "market" or "limit" order

volume: volume of the Trading Asset Pairs


