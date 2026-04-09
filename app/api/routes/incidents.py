from uuid import uuid4

from fastapi import APIRouter, HTTPException

from app.schemas.incidents import IncidentCreate, IncidentResponse, IncidentUpdate

router = APIRouter(prefix="/incidents", tags=["incidents"])

incidents_db: dict[str, IncidentResponse] = {}


@router.post("/", response_model=IncidentResponse, status_code=201)
def create_incident(payload: IncidentCreate) -> IncidentResponse:
    incident = IncidentResponse(
        id=str(uuid4()),
        title=payload.title,
        description=payload.description,
        service=payload.service,
        severity=payload.severity,
        status=payload.status,
    )

    incidents_db[incident.id] = incident
    return incident


@router.get("/", response_model=list[IncidentResponse])
def list_incidents() -> list[IncidentResponse]:
    return list(incidents_db.values())


@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(incident_id: str) -> IncidentResponse:
    incident = incidents_db.get(incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    return incident


@router.patch("/{incident_id}", response_model=IncidentResponse)
def update_incident(incident_id: str, payload: IncidentUpdate) -> IncidentResponse:
    incident = incidents_db.get(incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    updated_data = incident.model_dump()
    changes = payload.model_dump(exclude_unset=True)
    updated_data.update(changes)

    updated_incident = IncidentResponse(**updated_data)
    incidents_db[incident_id] = updated_incident

    return updated_incident

@router.delete("/{incident_id}", status_code=204)
def delete_incident(incident_id: str) -> None:
    incident = incidents_db.get(incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    del incidents_db[incident_id]
