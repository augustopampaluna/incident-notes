from typing import Literal

from pydantic import BaseModel


Severity = Literal["low", "medium", "high", "critical"]
Status = Literal["open", "in_progress", "resolved"]


class IncidentCreate(BaseModel):
    title: str
    description: str | None = None
    service: str
    severity: Severity
    status: Status


class IncidentUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    service: str | None = None
    severity: Severity | None = None
    status: Status | None = None


class IncidentResponse(BaseModel):
    id: str
    title: str
    description: str | None = None
    service: str
    severity: Severity
    status: Status