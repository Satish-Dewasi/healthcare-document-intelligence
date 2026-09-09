from fastapi import FastAPI

from src.api.routes import router

app = FastAPI()

app.include_router(router)


@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "service": "ml-service"
    }