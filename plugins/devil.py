import random, re

import asyncio
from telethon import events

@bot.message_handler(commands=["devil"])
def send_message(message):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("😒You Know I'm a good **PERSON**😏")
        await asyncio.sleep(1.9)
        await event.edit("BUT😡")
        await asyncio.sleep(1.2)
        await event.edit("😑Don't give me a reason😠")
        await asyncio.sleep(1.9)
        await event.edit("🤨To show my😎")
        await asyncio.sleep(1.4)
        await event.edit("**😈DEVIL SIDE**😈")
        await asyncio.sleep(1.3)
        await event.edit("**😈YOU KNOW THAT I'M A GOOD PERSON. BUT DON'T GIVE ME REASON TO SHOW MY EVIL SIDE😈**")
        await asyncio.sleep(2.1)
        await event.edit("**👿🇱🇰 Im WhiteDevil's YT Song Downloader Bot 😂🇱🇰**")
        await asyncio.sleep(1.3)
        await event.edit("**Lol😂 Im Only Bot 😂 I Dont Talk With You 😂**")





