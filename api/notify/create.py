from decimal import Decimal

# // pydentic
class CreateNotificationAssetPricing:
    asset_pricing: Decimal
    current_market_price: Decimal
    daily_trading_vol: Decimal
    high_price_day: Decimal
    low_price_day: Decimal

def create(req):
    NotificationStore().create
    create()
    processed_req(req)
    