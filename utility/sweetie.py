import datetime
import const
import random
from utility.wx_work import messenger
from .tz import Asia_Shanghai

re_choose_url = f"{const.site}/rechoose"


def get_choices():
    for direction in const.choices:
        for foods in const.choices["direction"]:
            yield (direction, foods)


def choose():
    food_choices = list(get_choices())
    direction, food = random.choices(food_choices)
    return direction, food


def serve():
    item = check_choose_time()
    if not item[0]:
        return 

    time_map = {
        "AM": "午",
        "PM": "晚"
    }
    time = time_map[item[1]]
    direction, food = choose()
    push(direction=direction, food=food)
    return direction, food 


def re_choose(time):
    direction, food = choose()
    push(direction=direction, food=food, rechoose=True)
    return direction, food


def push(direction, food, time="", rechoose=False):
    prefix = f"马上到吃{time}饭时间啦，今日建议"
    if rechoose:
        prefix = "已重新选择, 建议"
    msg = (
        f'{prefix}<font color="info">{direction}</font>的<font color="info">{food}</font>\n'
        f'还可以：\n'
        f'>[重新选择]({re_choose_url})'
    )
    messenger.send(msg)


def check_choose_time():
    now = datetime.datetime.now(tz=Asia_Shanghai)
    if 11 <= now.hour <= 12:
        return True, "AM"
    elif 18 <= now.hour <= 19:
        return True, "PM"
    else:
        return False, ""
