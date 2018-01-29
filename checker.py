#!/usr/bin/python
#-*- codong: utf-8 -*- 
import requests
import json
from coincheck import market, order
from sender import Line

ma = market.Market()

URL = "https://coincheck.com/api/rate/"

#coins = {"XEM": "xem_jpy", "XRP": "xrp_jpy"} #multi
coins = {"BTC": "btc_jpy"} #sigle

if __name__ == '__main__':
    message = ""
    for key,item in coins.items():
        #get coincheck's rate
        coincheck = requests.get(URL+item).json()
        
        #inform line
        Line().sender(key + " is " + coincheck["rate"] + " jpy")

        #process only for specific coin 
        if key == "XRP":
            if(float(coincheck.item) > 200.0):
                Line().sender("XRP over 155 yen" + coincheck["rate"])


