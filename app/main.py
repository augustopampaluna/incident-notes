from fastapi import FastAPI
from app.api.routes.incidents import router as incidents_router
from app.api.routes.system import router as system_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)

app.include_router(system_router)
app.include_router(incidents_router)