from fastapi import APIRouter
from app.schemas.fact_schema import (
    FactCreate,
    FactUpdate
)
from app.repositories.fact_repositories import FactRepository

router = APIRouter(
    prefix="/facts",
    tags=["Facts"]
)

@router.post("/")
async def create_fact(
    fact: FactCreate
):

    fact_id = await FactRepository.create_fact(
        fact.model_dump()
    )

    return {
        "message": "Fact created",
        "fact_id": fact_id
    }


@router.get("/")
async def get_all_facts():

    return await FactRepository.get_all_facts()


@router.get("/{fact_id}")
async def get_fact(
    fact_id: str
):

    return await FactRepository.get_fact_by_id(
        fact_id
    )


@router.put("/{fact_id}")
async def update_fact(
    fact_id: str,
    fact: FactUpdate
):

    await FactRepository.update_fact(
        fact_id,
        fact.content
    )

    return {
        "message": "Fact updated"
    }


@router.delete("/{fact_id}")
async def delete_fact(
    fact_id: str
):

    await FactRepository.delete_fact(
        fact_id
    )

    return {
        "message": "Fact deleted"
    }