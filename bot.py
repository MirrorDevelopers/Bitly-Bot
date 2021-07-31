"""
Bitly url shortner bot
Copyright (C) 2021 @ImJanindu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Kang with credits vomro

import os
import logging
from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import bitlyshortener
from sample_config import Config

# logging
bot = Client(
   "Bitly",
   api_id=Config.API_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)

# Bitly login
token = [Config.BITLY_TOKEN]
shortener = bitlyshortener.Shortener(tokens=token, max_cache_size=256)


# start msg
@bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
   user = message.from_user.mention
   return await message.reply_text(f"""Hey {user}, I am **Bitly Bot** ✨
I can short urls via bit.ly 💥
Send a long url to shorten it 😇""",
   reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Source Code 💻", url="https://github.com/ImJanindu/Bitly-Bot")]]))


# Function
@bot.on_message(filters.regex(pattern="https://") & filters.private)
async def short(_, message):
    input = [message.text]
    msg = await message.reply_text("`Shortening url...`")
    try:
        output = shortener.shorten_urls(input)
    except:
        return await msg.edit("`Error.`")
    link = ''.join(output)
    return await msg.edit(link)


bot.start()
idle()
