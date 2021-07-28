from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from vars import var


START_MSG = """
Hi, I am **ANONYMOUS SENDER BOT.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!\n
Note - We Dont Promote Circulation of
Copyright Contents. This Bot is
Created for Educational Purpose
Only !!

Please Support The Developer
By Joining the Support Channel👇👇

~ Made by @FZBOTS 🇱🇰
"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("👥 Group",
                          url="https://t.me/FilmsZillaUpdate_new")],
    [InlineKeyboardButton("🔊 Channel",
                          url="https://t.me/FZBOTS")]])


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)
