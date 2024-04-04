from fastapi import APIRouter

from src.init import cmc_client


router = APIRouter(
    prefix="/currencies"
)


@router.get("")
async def get_currencies():
    return await cmc_client.get_listings()

@router.get("/{currency_id}")
async def get_currency(currency_id: int):
    return await cmc_client.get_currency(int(currency_id))