
from api.notify.create import create


create_notify_dict = {
          "asset_pricing": 100,
          "current_market_price": 353,
          "daily_trading_vol": 143434,
          "high_price_day": 360,
          "low_price_day": 345      
        }
def server():
    create_resp = create(create_notify_dict)
    print(create_resp)
    

if __name__ == "__main__":
    print("server init")
    server()

