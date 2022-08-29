# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Recode @VckyouuBitch
# FROM GeezProjects <https://github.com/vckyou/GeezProjects>
# Copyright © 2021-2022

import random
import time
from datetime import datetime

from speedtest import Speedtest

from geezproject import CMD_HANDLER as cmd
from geezproject import CMD_HELP, StartTime, bot
from geezproject.events import register
from geezproject.utils import edit_or_reply, humanbytes, geez_cmd

absen = [
    "**Hadir bang** 😁",
    "**Hadir kak** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@geez_cmd(pattern="ping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(ping, "**Pinging.**")
    await xx.edit("**Pinging..**")
    await xx.edit("**Pinging...**")
    await xx.edit("**Pinging....**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await ping.client.get_me()
    await xx.edit(f"**Gojo - Userbot Runtime**\n**Pinger** : %sms\n**Bot Uptime** : {uptime}" % (duration))


@geez_cmd(pattern=r"xping$")
async def _(ping):
    """For .ping command, ping the gojouserbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await edit_or_reply(ping, "`Pinging....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**PONGGG!**\n**Pinger** : %sms\n**Bot Uptime** : {uptime}" % (duration)
    )


@geez_cmd(pattern=r"keping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await edit_or_reply(pong, "**『⍟𝐊𝐎𝐍𝐓𝐎𝐋』**")
    await kopong.edit("**◆◈PINGGGG◈◆**")
    await kopong.edit("**BENTARR**")
    await kopong.edit("**☬LANJUTTT☬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await bot.get_me()
    await kopong.edit(
        f"**✲ Woeylah** "
        f"\n ⫸ Tobat `%sms` \n"
        f"**✲ Beliau Lagi Tobat** "
        f"\n ⫸ Lagi Tobat『[{user.first_name}](tg://user?id={user.id})』 \n" % (duration)
    )


# .keping & kping Coded by Koala


@geez_cmd(pattern=r"kping$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await edit_or_reply(pong, "8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8==✊=D")
    await kping.edit("8=✊==D")
    await kping.edit("8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8==✊=D")
    await kping.edit("8=✊==D")
    await kping.edit("8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8===✊D")
    await kping.edit("8====D")
    await kping.edit("**PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit(
        f"**WOEYYY! 🐨**\n**PINGENG** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@geez_cmd(pattern="speedtest$")
async def _(speed):
    """For .speedtest command, use SpeedTest to check server speeds."""
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@geez_cmd(pattern="pong$")
async def _(pong):
    """For .ping command, ping the gojouserbot from any chat."""
    start = datetime.now()
    xx = await edit_or_reply(pong, "`PONG!.....🏓`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("🏓 **Ping!**\n`%sms`" % (duration))


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
@register(pattern=r"^\.absen$", sudo=True)
async def geez(ganteng):
    await ganteng.reply(random.choice(absen))


# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡


CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}ping` ; `{cmd}xping` ; `{cmd}kping`\
        \n  ❍▸ : **Untuk menunjukkan ping gojouserbot.\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}pong`\
        \n  ❍▸ : **Sama seperti perintah ping\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}speedtest`\
        \n  ❍▸ : **Untuk Mengetes kecepatan server gojouserbot.\
    "
    }
)
