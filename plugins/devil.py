import random, re

import asyncio
from telethon import events

@bot.message_handler(commands=["devil"])
def send_message(message):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("๐You Know I'm a good **PERSON**๐")
        await asyncio.sleep(1.9)
        await event.edit("BUT๐ก")
        await asyncio.sleep(1.2)
        await event.edit("๐Don't give me a reason๐ ")
        await asyncio.sleep(1.9)
        await event.edit("๐คจTo show my๐")
        await asyncio.sleep(1.4)
        await event.edit("**๐DEVIL SIDE**๐")
        await asyncio.sleep(1.3)
        await event.edit("**๐YOU KNOW THAT I'M A GOOD PERSON. BUT DON'T GIVE ME REASON TO SHOW MY EVIL SIDE๐**")
        await asyncio.sleep(2.1)
        await event.edit("**๐ฟ๐ฑ๐ฐ Im WhiteDevil's YT Song Downloader Bot ๐๐ฑ๐ฐ**")
        await asyncio.sleep(1.3)
        await event.edit("**Lol๐ Im Only Bot ๐ I Dont Talk With You ๐**")





