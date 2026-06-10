from fastapi import FastAPI
from app.routers.user_router import router as user_router

app = FastAPI(
    title="RAG Knowledge Management System"
)

app.include_router(user_router)


@app.get("/")
def home():
    return {
        "message": "Server Running"
    }