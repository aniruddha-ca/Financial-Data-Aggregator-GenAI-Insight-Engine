from datetime import datetime
from typing import List

class AssetData:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.prices: List[dict] = []

    def add_price(self, price: float):
        self.prices.append({"timestamp": datetime.utcnow(), "price": price})
        self.prices = [p for p in self.prices if (datetime.utcnow() - p["timestamp"]).days <= 7]

    def latest_price(self) -> float:
        return self.prices[-1]["price"] if self.prices else 0.0

    def change_percent_24h(self) -> float:
        if len(self.prices) < 2:
            return 0.0
        latest = self.prices[-1]["price"]
        for p in reversed(self.prices):
            if (datetime.utcnow() - p["timestamp"]).total_seconds() >= 86400:
                old_price = p["price"]
                return ((latest - old_price) / old_price) * 100
        return 0.0

    def average_price_7d(self) -> float:
        if not self.prices:
            return 0.0
        total = sum(p["price"] for p in self.prices)
        return total / len(self.prices)
