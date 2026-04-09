from datetime import datetime, timezone
from uuid import uuid4

from fastapi import HTTPException

from app.schemas.incidents import (
    IncidentCreate,
    IncidentNoteCreate,
    IncidentNoteResponse,
    IncidentResponse,
    IncidentUpdate,
)


incidents_db: dict[str, IncidentResponse] = {}


def create_incident(payload: IncidentCreate) -> IncidentResponse:
    now = datetime.now(timezone.utc)

    incident = IncidentResponse(
        id=str(uuid4()),
        title=payload.title,
        description=payload.description,
        service=payload.service,
        severity=payload.severity,
        status=payload.status,
        created_at=now,
        updated_at=now,
        notes=[],
    )

    incidents_db[incident.id] = incident
    return incident


def list_incidents() -> list[IncidentResponse]:
    return list(incidents_db.values())


def get_incident(incident_id: str) -> IncidentResponse:
    incident = incidents_db.get(incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    return incident


def update_incident(incident_id: str, payload: IncidentUpdate) -> IncidentResponse:
    incident = incidents_db.get(incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    updated_data = incident.model_dump()
    changes = payload.model_dump(exclude_unset=True)
    updated_data.update(changes)
    updated_data["updated_at"] = datetime.now(timezone.utc)

    updated_incident = IncidentResponse(**updated_data)
    incidents_db[incident_id] = updated_incident

    return updated_incident


def delete_incident(incident_id: str) -> None:
    incident = incidents_db.get(incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    del incidents_db[incident_id]


def add_note_to_incident(
    incident_id: str, payload: IncidentNoteCreate
) -> IncidentNoteResponse:
    incident = incidents_db.get(incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    note = IncidentNoteResponse(
        id=str(uuid4()),
        content=payload.content,
        created_at=datetime.now(timezone.utc),
    )

    updated_data = incident.model_dump()
    updated_data["notes"].append(note.model_dump())
    updated_data["updated_at"] = datetime.now(timezone.utc)

    updated_incident = IncidentResponse(**updated_data)
    incidents_db[incident_id] = updated_incident

    return note


def list_incident_notes(incident_id: str) -> list[IncidentNoteResponse]:
    incident = incidents_db.get(incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    return incident.notes
