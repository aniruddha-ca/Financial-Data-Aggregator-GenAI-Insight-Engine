from fastapi import APIRouter, HTTPException
from app.services import ingestion, metrics, summary
from app.api import schemas

router = APIRouter()

@router.get("/assets", response_model=list[schemas.Asset])
async def get_assets():
    return ingestion.get_tracked_assets()

@router.get("/metrics/{symbol}", response_model=schemas.Metrics)
async def get_metrics(symbol: str):
    data = metrics.get_metrics(symbol.upper())
    print("----")
    print(data)
    if not data:
        raise HTTPException(status_code=404, detail="Asset not found")
    return data

@router.get("/compare", response_model=schemas.Comparison)
async def compare_assets(asset1: str, asset2: str):
    comparison = metrics.compare_assets(asset1.upper(), asset2.upper())
    if not comparison:
        raise HTTPException(status_code=404, detail="One or both assets not found")
    return comparison

@router.get("/summary", response_model=schemas.Summary)
async def get_summary():
    return summary.generate_summary()

@router.post("/ingest")
async def ingest_data():
    await ingestion.ingest_data()
    return {"message": "Data ingestion triggered"}
