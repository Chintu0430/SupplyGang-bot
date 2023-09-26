#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>ᴅᴇᴠᴇʟᴏᴘᴇʀ:- <a href='tg://user?id={OWNER_ID}'>×͜× 𝙲𝙷𝙸𝙽𝚃𝚄 ࿐ ᶨᴿ</a>\nᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ:- <a href='https://t.me/moviessupplierofficial'>⚜️𝗠𝗢𝗩𝗜𝗘𝗦 𝗦𝗨𝗣𝗣𝗟𝗜𝗘𝗥 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟⚜️</a>\nʀᴇǫᴜᴇꜱᴛ ɢʀᴏᴜᴘ :- <a href='https://t.me/Moviessupplier90'>🎦𝐌𝐎𝐕𝐈𝐄𝐒 𝐒𝐔𝐏𝐏𝐋𝐈𝐄𝐑🎬</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
