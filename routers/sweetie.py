from fastapi import APIRouter
from utility import sweetie

router = APIRouter(prefix="/api")


@router.get("/rechoose")
async def re_choose():
    await sweetie.re_choose()
    return {"message": "已重新选择，消息已推送"}