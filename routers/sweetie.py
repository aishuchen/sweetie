from fastapi import APIRouter
from utility import sweetie

router = APIRouter(prefix="/api")


@router.get("/rechoose")
def re_choose():
    item = sweetie.check_choose_time()
    if item[0]:
        sweetie.re_choose()
        return {"message": "已重新选择，消息已推送"}
    else:
        return {"message": "没到饭点不要瞎玩哦，饿了多喝热水 ^_^"}