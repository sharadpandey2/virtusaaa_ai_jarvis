from fastapi import FastAPI

app = FastAPI(title="Liquidity AI & Anomaly Engine")

@app.get("/health")
def health():
    return {"status": "online"}
