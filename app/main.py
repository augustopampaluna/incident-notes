from fastapi import FastAPI
from app.api.routes.system import router as system_router
from app.api.routes.incidents import router as incidents_router

app = FastAPI(title="Incident Notes API")

app.include_router(system_router)
app.include_router(incidents_router)