import tool
import datetime

from khl.card import CardMessage, Card, Module, Element, Types
# from tools import bili
# from typing import Union, Dict, List


def get_info_card():
    info_color = tool.randomcolor()
    day_no = tool.getDays('2023-2-9')
    day_no1 = tool.getDays('2023-4-8')
    day_end = tool.getDays('2023-7-3')
    card = CardMessage(
        Card(
            Module.Header('📢 秦翔一建所今日公告'),
            Module.Divider(),
            Module.Context(f'🈲 今天是{datetime.date.today()}，秦部今天也在群里没事@人！'),
            Module.Context(f'⛑翔历Day{day_no}, 直播间封禁一年，好似！'),
            Module.Context(f'👽爽历Day{day_no1}, 有人晒卡当海豹，我不说是谁。'),
            Module.Divider(),
            Module.Section(
                f'虽然直播间没了{day_end}天 ，但说不定套皮复活。',
                Element.Button('北方火LINK', 'https://live.bilibili.com/860455', Types.Click.LINK)
            ),
            Module.Section(
                f'套皮复活回来吧，xg直播间，点击关注北方火喵。',
                Element.Button('小路绫直播间', 'https://live.bilibili.com/1176188', Types.Click.LINK)
            ),
            color=info_color
        ))
    return card


# async def get_live_card():
#     info_color = tool.randomcolor()
#     live_info = await bili.live_by_xll()
#
#     # "title":
#     # "live_id":
#     # "cover":
#     # "live_status":
#     # "live_start_time":
#     # "user_name":
#     # "user_cover":
#     card = CardMessage(
#         Card(
#             Module.Header(f'{live_info["user_name"]}直播间: 标题「{live_info["title"]}」'),
#             Module.Divider(),
#             Module.Context(f'状态: {live_info["live_status"]}，开始时间: {live_info["live_start_time"]}'),
#             Module.Section(
#                 f'',
#                 Element.Button(f'{live_info["user_name"]}的直播间', 'https://live.bilibili.com/1176188', Types.Click.LINK)
#             ),
#             color=info_color
#         ))
#     return card
