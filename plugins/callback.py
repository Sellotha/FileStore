from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import START_MSG, HELP_MSG, ABOUT_MSG, START_PIC
from bot import Bot

@Bot.on_callback_query()
async def handle_callback(bot: Client, query: CallbackQuery):
    data = query.data

    if data == "help":
        await query.message.edit_text(
            HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="home"),
                 InlineKeyboardButton("ᴄʟᴏsᴇ ✖", callback_data="close")]
            ])
        )

    elif data == "about":
        await query.message.edit_text(
            ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="home"),
                 InlineKeyboardButton("ᴄʟᴏsᴇ ✖", callback_data="close")]
            ])
        )

    elif data == "home":
        user = query.from_user
        await query.message.edit_caption(
            caption=START_MSG.format(
                first=user.first_name,
                last=user.last_name or "",
                username=f"@{user.username}" if user.username else "None",
                mention=user.mention,
                id=user.id
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• ᴍᴏʀᴇ ᴄʜᴀɴɴᴇʟs •", url="https://t.me/Nova_Flix/50")],
                [InlineKeyboardButton("• ᴀʙᴏᴜᴛ", callback_data="about"),
                 InlineKeyboardButton("ʜᴇʟᴘ •", callback_data="help")]
            ])
        )

    elif data == "close":
        try:
            await query.message.delete()
        except:
            await query.answer("Cannot close this message.", show_alert=True)
