from fastapi import FastAPI

app = FastAPI(
    title="Incident Notes API",
    description="API simple para practicar Azure con FastAPI y Cosmos DB",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {
        "message": "Incident Notes API is running"
    }


@app.get("/health")
def healthcheck():
    return {
        "status": "ok"
    }