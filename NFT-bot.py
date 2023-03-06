import requests
import json
import time
#------------------------------------------------------------------
bot_key = '*******************'
chat_id = '********'
#------------------------------------------------------------------
seuil = 42   # the seuil need to be changed in function of each of the 2 scenario  
time_interval = 5 
#------------------------------------------------------------------
def get_price():
    symbol = "Okay Bears"

    url = "http://api-mainnet.magiceden.dev/v2/collections/{symbol}/stats".format(symbol=symbol.lower().replace(" ", "_"))

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    nft_price = response['floorPrice'] / 1000000000 
    return nft_price, symbol  

def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def main():
    while True:
        
        floor_price, name = get_price()
        print(floor_price)
        print(name)
        if floor_price <= seuil:  # applicated for the seller and the buyer, if i am a seller and the floor price get closer to the seuil i will rise the price
            send_update(chat_id, f" Take your chance ! the price of the NFT collection {name} is :{floor_price}")
        else:
            send_update(chat_id, f"the price of the NFT collection {name} is :{floor_price}")  # can work with it if i need to know if the price of my collection is still above the mint price

        time.sleep(time_interval)
main()
