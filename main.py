import io
import json
import logging
import datetime
import time
import random

import tool
import qx_card

from khl import *
from khl.card import CardMessage, Card, Module, Element, Types, Struct
from random import randint
from tools import bili

# loading config and setting bot
with open('/www/wwwpy/config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
# with open('./config/config.json', 'r', encoding='utf-8') as f:
#     config = json.load(f)
logging.basicConfig(level='INFO')
bot = Bot(token=config['token'])


@bot.task.add_cron(hour=8, timezone="Asia/Shanghai")  # 每天8点执行
async def test_game_state():
    ch_id = config['channel_info']
    ch = await bot.client.fetch_public_channel(ch_id)
    # await ch.send(f'现在早八，今日公告。')
    cm = qx_card.get_info_card()
    await ch.send(cm)


"""
plan: 
    chrome headless
    playwright
"""
"""
    @bot.task.add_cron()        # 指定时间运行事件，比如每天0点干一次
    @bot.task.add_interval()    # 每设定时间运行一次，比如每30分钟执行一次；从bot开机开始计时
    @bot.task.add_date()        # 这个一般用来设置开机任务
    
    exec_req
    await bot.client.gate.exec_req(api.Channel.list(guild_id=guild_id))
"""


# async def dynamic(msg: Message):
#     img = await get_wish_screenshot()
#     img_url = await bot.upload_asset(io.BytesIO(img))


#  @bot.task.add_interval(hours=2)  # 每2小时执行
#  async def test_game_state():
#      ch_id = config['channel_info']
#      ch = await bot.client.fetch_public_channel(ch_id)
#      await ch.send(f'现在时间是:{datetime.datetime.now()}。')


#  '/dd': 手动发公告
@bot.command('ff')
async def card_daily(msg: Message):
    card = qx_card.get_info_card()
    await msg.ctx.channel.send(card)


# live
@bot.command(name='yy')
async def xll_live(msg: Message):
    card = await qx_card.get_live_card()
    await msg.ctx.channel.send(card)


@bot.on_event(EventTypes.ADDED_REACTION)
async def reaction_set_roles(b: Bot, event: Event):
    u = await b.client.fetch_user(config["user_id_llj"])


# use game_id to set bot gaming status
@bot.command(name='game-id')
async def status_gaming(msg: Message, game_id: int):
    # game_id : int
    await bot.client.update_playing_game(game_id)
    await msg.reply(f'秦工的图灵机器人在玩游戏！')


# set bot music status  添加音乐状态
@bot.command(name='mus')
async def status_music(msg: Message, music: str = 'チキチキバンバン', singer: str = 'V.A.'):
    tid = msg.author_id
    if tid == config["user_id_admin"]:
        # music_software : Enum ['cloudmusic'、'qqmusic'、'kugou']
        await bot.client.update_listening_music(music, singer, "cloudmusic")
        await msg.reply(f'秦工的图灵机器人在听{music} - {singer}！')
        # await msg.reply(f"access successfully")
    else:
        await msg.reply(f"无效的操作。")


# delete bot status  删除指定状态
@bot.command(name='stop')
async def status_stop(msg: Message, d: int):
    if d == 1:
        await bot.client.stop_playing_game()
    elif d == 2:
        await bot.client.stop_listening_music()
    await msg.reply('秦工的图灵机器人被关了。')


# delete bot status  删除所有状态
@bot.command(name='stop-all')
async def status_stop(msg: Message):
    await bot.client.stop_playing_game()
    await bot.client.stop_listening_music()
    await msg.reply('秦工的机器人休息了。')


# 投骰子
@bot.command(name='骰子')
async def com_tz(msg: Message):
    ran_num = randint(1, 6)
    text = '骰子点数 = ' + str(ran_num)
    await msg.reply(text)


# 测试命令
@bot.command(name='2023')
async def text_2023(msg: Message):
    text = 'XGNB2023'
    await msg.reply(text)


# 测试回复
@bot.command(name='色图')
async def text_setu(msg: Message):
    text = '秦工的图灵机器人提示你：你不许搞HS，工作室严查败坏风气！'
    await msg.reply(text)


# roll
@bot.command(name='roll')
async def com_roll(msg: Message, t_min: int, t_max: int, n: int = 1):
    result = [randint(t_min, t_max) for i in range(n)]
    await msg.reply(f'你投出了:{result}')


# 测试能否获取游戏状态
@bot.command(name='gamejsontest')
async def test_game_state(msg: Message):
    game_json = await bot.client.gate.request('GET', 'game')
    await msg.reply(game_json)


# 这是一个自定义规则, 用来判断是否msg和keyword相同
def is_contains(keyword: str):
    def func(msg: Message):
        return msg.content.find(keyword) != -1

    return func


# 这是一个例子, 需要输入/test_day yyyy-mm-dd 相同才可以触发
@bot.command(name='test_day', rules=[is_contains(str(datetime.date.today()))])
async def test_decorator(msg: Message, date: str):
    await msg.reply(f'yes! today is {date}')


# 测试获取用户ID
@bot.command(name='tid')
async def test_decorator(msg: Message):
    tid = msg.author_id
    await msg.reply(f'test code is {tid}')
    if tid == config["user_id_admin"]:
        await msg.reply(f"access successfully")
    else:
        await msg.reply(f"invalid access")


# 回应操作反馈
@bot.on_event(EventTypes.ADDED_REACTION)
async def reaction_reminder(b: Bot, event: Event):
    print(event.body)

    # fetch channel of the REACTION event
    channel = await b.client.fetch_public_channel(event.body['channel_id'])
    # send a message to inform user at current channel
    # await b.client.send(channel, f"你回应了{event.body['emoji']['id']}!")

    # send a message to inform user at current channel
    # only visible to `event.body['user_id']`
    await b.client.send(channel, f"你回应了{event.body['emoji']['id']}(此消息仅你可见)",
                        temp_target_id=event.body['user_id'])


# starting bot
bot.run()
