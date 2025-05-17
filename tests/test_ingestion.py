import pytest
from app.services import ingestion

@pytest.mark.asyncio
async def test_ingest_data():
    await ingestion.ingest_data()
    assets = ingestion.get_tracked_assets()
    assert len(assets) > 0
