# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

# By New-Dev0 (@TeamUltroid)

import os
import asyncio
import glob
from random import choice, randrange, shuffle
from . import ultroid_cmd, get_string
from pyUltroid.functions.google_image import googleimagesdownload

TEXT = ["Happy Holi", "Happy Holi to ALL!", "May this Holi fill your life with bright colours!", "Enjoy Playing with colours",
    "May this Holi, bring lot of enjoyment to your life!", "Happy Holi\nStay Safe stay Life!", "Color your friends with color this Holi!"]


@ultroid_cmd(pattern="holi$")
async def wish_dar_holi(ultroid):
    msg = await ultroid.eor(get_string("com_1"))
    if not os.path.exists("happy holi"):
        im = googleimagesdownload()
        keywords = {"keywords":"happy holi", "format":"jpg", "limit": randrange(30, 50), "output_directory":"."}
        dl = await im.download(keywords)
        images = dl[0]["happy holi"]
        shuffle(images)
        imgs = images[:randrange(5, 8)]
    else:
        imgs = glob.glob("happy holi/*jpg")
        if not imgs:
            return await msg.delete()
        shuffle(imgs)
        imgs = imgs[:randrange(5, 6)]
    text = choice(TEXT)
    await msg.delete()
    nkk = await ultroid.client.send_message(ultroid.chat_id, text, file=imgs[0])
    imgs = imgs[1:]
    for img in imgs:
        await nkk.edit(file=img)
        await asyncio.sleep(2.5)