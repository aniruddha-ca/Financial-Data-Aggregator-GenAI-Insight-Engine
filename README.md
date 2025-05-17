# 📊 Financial Data Aggregator & GenAI Insight Engine

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aniruddha-ca/Financial-Data-Aggregator-GenAI-Insight-Engine.git
```

### 2. Create a Virtual Environment

```bash
python3.10 -m venv venv-finance-insights
source venv-finance-insights/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the App

### 1. Setup Env

Create .env add Open AI api key
```
OPENAI_API_KEY=<open_api_key>
```

### 2. Run Fastapi


```bash
uvicorn app.main:app --reload
```

Visit API Docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Run Tests

```bash
PYTHONPATH=. pytest
```

---

## Developed By

**Aniruddha Chaudhari**  
Email: aniruddha.ca@gmail.com  
Profile: [https://www.csestack.org/anirudh/](https://www.csestack.org/anirudh/)

---
