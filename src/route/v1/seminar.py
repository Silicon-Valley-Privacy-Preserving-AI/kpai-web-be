from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.config.database import get_db
from fastapi import HTTPException, status

from src.model import User
from src.route.v1.user import get_current_user
from src.service.seminar_service import SeminarService
from src.schema.seminar import (
    SeminarCreateRequest,
    SeminarModifyRequest,
    SeminarResponse,
    SeminarDetailResponse
)

router = APIRouter(prefix="/seminars", tags=["Seminar"])


async def get_seminar_service(
    db: AsyncSession = Depends(get_db)
):
    return SeminarService(db)


@router.get(
    "",
    summary="Get seminar list",
    response_model=list[SeminarResponse]
)
async def get_seminars(
    seminar_service: SeminarService = Depends(get_seminar_service)
):
    return await seminar_service.get_seminars()


@router.get(
    "/{seminar_id}",
    summary="Get seminar detail",
    response_model=SeminarDetailResponse
)
async def get_seminar(
    seminar_id: int,
    seminar_service: SeminarService = Depends(get_seminar_service)
):
    seminar = await seminar_service.get_seminar_detail(seminar_id)

    if seminar is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No seminar found"
        )

    return seminar


@router.post(
    "",
    summary="Create seminar",
    response_model=SeminarResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_seminar(
    seminar_data: SeminarCreateRequest,
    seminar_service: SeminarService = Depends(get_seminar_service)
):
    return await seminar_service.create_seminar(seminar_data)


@router.put(
    "/{seminar_id}",
    summary="Modify seminar"
)
async def modify_seminar(
    seminar_id: int,
    seminar_data: SeminarModifyRequest,
    seminar_service: SeminarService = Depends(get_seminar_service)
):
    seminar = await seminar_service.get_seminar_by_id(seminar_id)
    return await seminar_service.modify_seminar(seminar, seminar_data)


@router.delete(
    "/{seminar_id}",
    summary="Delete seminar"
)
async def delete_seminar(
    seminar_id: int,
    seminar_service: SeminarService = Depends(get_seminar_service)
):
    seminar = await seminar_service.get_seminar_by_id(seminar_id)
    return await seminar_service.delete_seminar(seminar)


@router.post(
    "/{seminar_id}/rsvp",
    summary="RSVP for seminar"
)
async def rsvp_seminar(
    seminar_id: int,
    current_user: User = Depends(get_current_user),
    seminar_service: SeminarService = Depends(get_seminar_service)
):
    seminar = await seminar_service.get_seminar_by_id(seminar_id)
    if seminar is None:
        raise HTTPException(status_code=404, detail="Seminar not found")

    return await seminar_service.rsvp(seminar, current_user)


@router.delete(
    "/{seminar_id}/rsvp",
    summary="Cancel rsvp for seminar"
)
async def cancel_rsvp_seminar(
    seminar_id: int,
    current_user: User = Depends(get_current_user),
    seminar_service: SeminarService = Depends(get_seminar_service)
):
    seminar = await seminar_service.get_seminar_by_id(seminar_id)
    if seminar is None:
        raise HTTPException(status_code=404, detail="Seminar not found")

    return await seminar_service.cancel_rsvp(seminar, current_user)