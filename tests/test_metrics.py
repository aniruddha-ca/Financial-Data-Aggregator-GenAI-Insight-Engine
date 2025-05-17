from app.services import metrics

def test_get_metrics():
    data = metrics.get_metrics("BTC")
    assert data is not None
    assert data.symbol == "BTC"
