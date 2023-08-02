import asyncio
from tool import ts2time
from bilibili_api import video, live, sync


async def main() -> None:
    info = await live_by_xll()


async def video_from_bv(uid: int = 2022043):
    v = video.Video(bvid="BV1tk4y13716")  # 赋予Video类属性
    info = await v.get_info()  # 获取视频相关信息
    print(info["title"])


async def live_by_xll():
    l = live.LiveRoom(room_display_id=1176188)
    l_info = await l.get_room_info()

    # 'live_status': 0,  0: 未开播  1: 开播
    # 'live_start_time': 0,  0: 未开播;  sample: 1690965871
    # 'cover': 'http://i0.hdslb.com/bfs/live/new_room_cover/3379485cf18fe8005865ae3cac07148f50fd3930.jpg',

    room_info = l_info["room_info"]
    user_info = l_info["anchor_info"]
    user_base_info = user_info["base_info"]

    status = "未开播" if room_info["live_status"] == 0 else "开播中"
    start_time = ts2time(room_info["live_start_time"]) if room_info["live_start_time"] != 0 else "未开始"

    live_info = {
        "title": room_info["title"],
        "live_id": room_info["room_id"],
        "cover": room_info["cover"],
        "live_status": status,
        "live_start_time": start_time,
        "user_name": user_base_info["uname"],
        "user_cover": user_base_info["face"],
    }
    # print(live_info)
    return live_info


def live_info_xll():
    info = live_info_xll()
    return info


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
