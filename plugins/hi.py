@ultroid_cmd(pattern="hi ?(.*)")
async def hi(event):
    giveVar = event.text
    ult = giveVar[4:5]
    if not ult:
        ult = "đş"
    await edit_or_reply(
        event,
        f"{ult}â¨â¨{ult}â¨{ult}{ult}{ult}\n{ult}â¨â¨{ult}â¨â¨{ult}â¨\n{ult}{ult}{ult}{ult}â¨â¨{ult}â¨\n{ult}â¨â¨{ult}â¨â¨{ult}â¨\n{ult}â¨â¨{ult}â¨{ult}{ult}{ult}\nââââââââ",
    )