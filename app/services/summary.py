
from app.services.ingestion import asset_store
from app.core.config import TRACKED_ASSETS

# def generate_summary():
#     summaries = []
#     for symbol, asset in asset_store.items():
#         change = asset.change_percent_24h()
#         avg_price = asset.average_price_7d()
#         summaries.append(f"{TRACKED_ASSETS[symbol]} ({symbol}) saw a {change:.2f}% change over the last 24 hours, with a 7-day average price of ${avg_price:.2f}.")
#     return {"summary": " ".join(summaries)}



from openai import OpenAI
import os

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key="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")

def generate_summary():
    from app.services.ingestion import asset_store
    from app.core.config import TRACKED_ASSETS

    summaries = []
    for symbol, asset in asset_store.items():
        change = asset.change_percent_24h()
        avg_price = asset.average_price_7d()
        summaries.append(
            f"{TRACKED_ASSETS[symbol]} ({symbol}) had a {change:.2f}% 24h change "
            f"and a 7-day average price of ${avg_price:.2f}."
        )

    prompt = "Summarize the market trends:\n" + "\n".join(summaries)

    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial analyst summarizing crypto and stock market data."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return {"summary": chat_completion.choices[0].message.content.strip()}
