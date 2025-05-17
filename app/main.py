from dotenv import load_dotenv
from fastapi import FastAPI
from app.api.routes import router as api_router

load_dotenv()

app = FastAPI(title="Financial Data Aggregator & GenAI Insight Engine")

app.include_router(api_router)
