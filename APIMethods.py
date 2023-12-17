import mysql.connector
from mysql.connector import errorcode

import yfinance as yf
import pandas as pd
import random
import json
from algomojo.pyapi import *
import logging

logger = logging.getLogger(__name__)

def getQuote(userId, stkSym, brCode, stkExchange):
    try:
        con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='ty_live_proj_stock_automation_sys')
        cursor = con.cursor()

        query = f"""select apiKey, apiSecretKey from customer_details where userId = '{userId}'"""
        print(query)
        cursor.execute(query)
        for (key, sKey) in cursor:
            apiKey = key
            apiSecretKey = sKey            

        print(apiKey, apiSecretKey)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print("error:",err)
    finally:
        cursor.close()
        con.close()

    algomojo= api(api_key = apiKey, api_secret = apiSecretKey)
    try:
        response = algomojo.GetQuote(broker=brCode, symbol=stkSym, exchange=stkExchange) 
        print (response)
        return json.dumps(response)
    except Exception as e:
        logger.error(f"An error occurred: {e}")  
    
def getQuote2(userId, stkSym, brCode, stkExchange):
    return json.dumps({
        "status": "success",
        "data": {
                "symbol_name": stkSym,
                "trading_symbl": "YESBANK-EQ",
                "company_name": "YES BANK LIMITED",
                "last_trade_time": "06/01/2022 15:59:58",
                "last_price": float("{:.2f}".format(random.uniform(10,110))),
                "change": 00.00,
                "change_per": 00.00,
                "last_quantity": 4,
                "buy_quantity": 4,
                "sell_quantity": 303792,
                "volume": 125481711,
                "average_price": 14.26,
                "open": 14.25,
                "high": 14.45,
                "low": 14.10,
                "close": 14.25,
                "tick_size": 5,
                "multiplier": 1,
                "lot_size": 1,
                "decimalprecision": 2,
                "yearly_low_price": 10.50,
                "yearly_high_price": 18.60,
                "exchange": "NSE",
                "token": "11915"
            }
    })

def getQuoteFromYfinance(userId, stkSym, brCode, stkExchange):
    try:
        stk = yf.Ticker(stkSym+".NS")
        df = stk.history(period="1d", interval = '1d')
        return df
    except Exception as e:
        print(e)
    
    return pd.DataFrame({'Open':0, 'Close':0, 'High':0, 'Low':0})


def getHoldings2():
    # return json.dumps({"status": "success","data": []})
    return json.dumps({
        "status": "success",
        "data": [
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE1",
                "isin": "INE731H01025",
                "holdqty": 150,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,14))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE2",
                "isin": "INE731H01025",
                "holdqty": 80,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,16))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE3",
                "isin": "INE731H01025",
                "holdqty": 250,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,10))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE4",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,20))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE5",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,10))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE6",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,8))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE7",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,12))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE8",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,17))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE9",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,9))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE10",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,14))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE11",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,13))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE12",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,8))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE13",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 864,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,5))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE14",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,20))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            },
            {
                "exchange": "NSE",
                "token": "3478273",
                "symbol": "ACE15",
                "isin": "INE731H01025",
                "holdqty": 135,
                "btst_qty": 0,
                "sellable_qty": 0,
                "average_price": 323.6,
                "ltp": 31.85,
                "product": "CNC",
                "coll_qty": 0,
                "coll_type": "",
                "invest_val": 47377.5,
                "hld_val": 47377.5,
                "PL": float("{:.2f}".format(random.uniform(-80,10))),
                "broker_exchange": "BSE",
                "broker_token": "3478273",
                "tick_size": 0,
                "lot_size": 0,
                "holdtype": "HLD",
                "ws_msg": {
                        "exchange": "BSE",
                        "token": "3478273"
                }
            }
        ]
    })
