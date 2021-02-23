import datetime
import const
import random

from utility.wx_work import messenger

re_choose_url = f"{const.site}/rechoose"


def choose():
    direction = random.choice(tuple(const.choices.keys()))
    food = random.choice(const.choices[direction])
    return direction, food


async def serve():
    direction, food = choose()
    push(direction=direction, food=food)
    return food


async def re_choose():
    direction, food = choose()
    push(direction=direction, food=food, rechoose=True)
    return food


def push(direction, food, time="", rechoose=False):
    now = datetime.datetime.now()
    if 11 <= now.hour <= 12:
        time = "午"
    elif 18 <= now.hour <= 19:
        time = "晚"
    prefix = f"马上到吃{time}饭时间啦，今日建议"
    if rechoose:
        prefix = "已重新选择, 建议"
    msg = (
        f'{prefix}<font color="info">{direction}</font>的<font color="info">{food}</font>\n'
        f'还可以：\n'
        f'>[重新选择]({re_choose_url})'
    )
    messenger.send(msg)


if __name__ == '__main__':
    serve()