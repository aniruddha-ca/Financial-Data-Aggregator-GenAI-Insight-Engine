import yfinance as yf
from app.core.config import TRACKED_ASSETS
from app.models.asset_data import AssetData

asset_store = {symbol: AssetData(symbol) for symbol in TRACKED_ASSETS}

async def ingest_data():
    for symbol in TRACKED_ASSETS:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", interval="1h")
        # Returns a DataFrame with hourly data for past 24 hours.
        # Example:
        # Datetime              Open    High    Low     Close   Volume
        # 2025-05-15 10:00:00   171.1  173.2    170.9   172.8   1200000
        # 2025-05-15 11:00:00   172.9  174.0    172.5   173.6   1100000
        if not data.empty:
            latest_price = data["Close"].iloc[-1]
            asset_store[symbol].add_price(latest_price)

def get_tracked_assets():
    return [{"symbol": symbol, "name": name} for symbol, name in TRACKED_ASSETS.items()]
