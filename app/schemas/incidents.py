from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field

Severity = Literal["low", "medium", "high", "critical"]
Status = Literal["open", "in_progress", "resolved"]


class IncidentNoteCreate(BaseModel):
    content: str


class IncidentNoteResponse(BaseModel):
    id: str
    content: str
    created_at: datetime


class IncidentCreate(BaseModel):
    title: str
    description: str | None = None
    service: str
    severity: Severity
    status: Status = "open"


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
    created_at: datetime
    updated_at: datetime
    notes: list[IncidentNoteResponse] = Field(default_factory=list)