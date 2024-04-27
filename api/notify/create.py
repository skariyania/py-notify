from decimal import Decimal

from store.notification_store import NotificationStore

# // pydentic
class CreateNotificationAssetPricing:
    asset_pricing: Decimal
    current_market_price: Decimal
    daily_trading_vol: Decimal
    high_price_day: Decimal
    low_price_day: Decimal

def create(req):
    store = NotificationStore()
    notification_store_resp = store.create(req)
    return notification_store_resp
