from fastapi import APIRouter

from app.schemas.incidents import (
    IncidentCreate,
    IncidentNoteCreate,
    IncidentNoteResponse,
    IncidentResponse,
    IncidentUpdate,
)
from app.services import incidents as incident_service

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.post("/", response_model=IncidentResponse, status_code=201)
def create_incident(payload: IncidentCreate) -> IncidentResponse:
    return incident_service.create_incident(payload)


@router.get("/", response_model=list[IncidentResponse])
def list_incidents() -> list[IncidentResponse]:
    return incident_service.list_incidents()


@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(incident_id: str) -> IncidentResponse:
    return incident_service.get_incident(incident_id)


@router.patch("/{incident_id}", response_model=IncidentResponse)
def update_incident(incident_id: str, payload: IncidentUpdate) -> IncidentResponse:
    return incident_service.update_incident(incident_id, payload)


@router.delete("/{incident_id}", status_code=204)
def delete_incident(incident_id: str) -> None:
    incident_service.delete_incident(incident_id)


@router.post("/{incident_id}/notes", response_model=IncidentNoteResponse, status_code=201)
def add_note_to_incident(
    incident_id: str, payload: IncidentNoteCreate
) -> IncidentNoteResponse:
    return incident_service.add_note_to_incident(incident_id, payload)


@router.get("/{incident_id}/notes", response_model=list[IncidentNoteResponse])
def list_incident_notes(incident_id: str) -> list[IncidentNoteResponse]:
    return incident_service.list_incident_notes(incident_id)