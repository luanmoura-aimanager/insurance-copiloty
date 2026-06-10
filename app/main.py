from fastapi import FastAPI, Depends
from sqlalchemy import text
from app.db import get_session

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/health/db")
async def health_db(session=Depends(get_session)):
    await session.execute(text("SELECT 1"))
    return {"db": "ok"}
