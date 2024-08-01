import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import IMG, OWNER_USERNAME, STICKER
from BrandedAi import Branded
from BrandedAi.database.chats import add_served_chat
from BrandedAi.database.users import add_served_user
from BrandedAi.modules.helpers import PNG_BTN


@Branded.on_cmd("ping")
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{Branded.name} ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>|| мαdє ωιтн ❣️ ву [•─┼ᶦϻͣ|| 💖♡ ᴢɪᴅᴅɪ_ꜱʜᴀʏᴀʀ ♡💖 ||](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
