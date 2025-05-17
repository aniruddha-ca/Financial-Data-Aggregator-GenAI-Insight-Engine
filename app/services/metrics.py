from app.services.ingestion import asset_store
from app.api.schemas import Metrics, Comparison

def get_metrics(symbol: str):
    asset = asset_store.get(symbol)
    if not asset:
        return None
    return Metrics(
        symbol=symbol,
        latest_price=asset.latest_price(),
        change_percent_24h=asset.change_percent_24h(),
        average_price_7d=asset.average_price_7d()
    )

def compare_assets(asset1_symbol: str, asset2_symbol: str):
    asset1_metrics = get_metrics(asset1_symbol)
    asset2_metrics = get_metrics(asset2_symbol)
    if not asset1_metrics or not asset2_metrics:
        return None
    return Comparison(asset1=asset1_metrics, asset2=asset2_metrics)
