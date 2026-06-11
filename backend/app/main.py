from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.routers.fact_router import router as fact_router
from app.routers.auth_router import router as auth_router


app = FastAPI(
    title="RAG Knowledge Management System"
)

app.include_router(user_router)
app.include_router(fact_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "Server Running"
    }