from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status
from sqlmodel import select

from ..dependencies import SessionDependency
from ..enums import StatusEnum
from ..models import Incident
from ..schemas import IncidentCreate, IncidentDB, IncidentUpdate

router = APIRouter(
    prefix="/api"
)


@router.post("/incidents", response_model=IncidentDB)
async def create_incident(incident_request: IncidentCreate, session: SessionDependency):
    incident = Incident(**incident_request.model_dump())
    session.add(incident)
    await session.commit()
    await session.refresh(incident)
    return incident


@router.get("/incidents", response_model=list[IncidentDB])
async def get_incidents(
    session: SessionDependency,
    status_filter: Annotated[StatusEnum | None, Query(alias="status-filter")] = None
):
    if status_filter:
        results = select(Incident).where(Incident.status == status_filter).order_by(Incident.creation_date_time.desc())
    else:
        results = select(Incident).order_by(Incident.creation_date_time.desc())
    return await session.exec(results)


@router.patch("/incidents/{incident_id}", response_model=IncidentDB)
async def update_incident_status(
    session: SessionDependency,
    incident_id: int,
    incident_status: IncidentUpdate,
):
    incident = await session.get(Incident, incident_id)
    if not incident:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incident not found")
    incident.status = incident_status.status
    session.add(incident)
    await session.commit()
    await session.refresh(incident)
    return incident
