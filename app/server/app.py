from fastapi import FastAPI
from app.server.routes.accounts import router as AccountRouter
app = FastAPI()

app.include_router(AccountRouter, tags=["Accounts"], prefix="/accounts")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}