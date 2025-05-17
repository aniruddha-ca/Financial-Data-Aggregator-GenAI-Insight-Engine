from pydantic import BaseModel

class Asset(BaseModel):
    symbol: str
    name: str

class Metrics(BaseModel):
    symbol: str
    latest_price: float
    change_percent_24h: float
    average_price_7d: float

class Comparison(BaseModel):
    asset1: Metrics
    asset2: Metrics

class Summary(BaseModel):
    summary: str
