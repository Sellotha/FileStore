# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
APP_ID = int(os.environ.get("APP_ID")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002172427490")) #Your db channel Id
OWNER = os.environ.get("OWNER", "@thakur_m_10") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "5764304134")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8080")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://chamelisarkar235:1hI4NRjIF4EPYClS@cluster0.ck9u0.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster8090")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "http://t.me/Fedbk_rep_bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://i.postimg.cc/W4W2WV5h/IMG-20250723-085849.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.postimg.cc/VNGvLf2D/Moon-Knight.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b>ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ᴏᴜʀ ʜᴇʟᴘ ᴀɴᴅ ʀᴇᴘᴏʀᴛ ʙᴏᴛ <a href='https://t.me/Fedbk_rep_bot'>@Fedbk_rep_bot</a></b>\n\n<blockquote>“sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʟɪɴᴋ, sᴛᴀʀᴛ ᴛʜᴇ ʜᴇʟᴘ ʙᴏᴛ, ᴀɴᴅ ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴍᴇꜱꜱᴀɢᴇ ᴜꜱ...!”</blockquote>"
ABOUT_TXT = "<b><blockquote>◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/Name_huh'>𝐍𝐀𝐌𝐄_𝐇𝐔𝐇!</a>\n◈ ᴄʜᴀᴛ ɢʀᴏᴜᴘ: <a href='https://t.me/movie_talk_Group'>𝐌𝐨𝐯𝐢𝐞 𝐓𝐚𝐥𝐤 ֶָ֢ [𝐆𝐫𝐨𝐮𝐩]</a>\n◈ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/+X5RPKIsoDgtlZGFl'>𝐌𝐎𝐕𝐈𝐄 𝐓𝐀𝐋𝐊 ֶָ֢ 𓃮</a>\n◈ ʙᴀᴄᴋᴜᴘ: <a href='https://t.me/movie_talk_backup'>MOVIE TALK ֶָ֢ [BACKUP]</a>\n◈ ᴍᴏᴅᴇʀᴀᴛᴏʀ: <a href='https://t.me/lucifer_movie_talk'>𝐌𝐎𝐃𝐄𝐑𝐀𝐓𝐎𝐑 ֶָ֢ ⚡</a></blockquote></b>"
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<blockquote>ʜᴇʏ {first} ✨</blockquote>\n\n<b>ɪ ᴀᴍ ʜᴏꜱᴘᴇʀ x — ʏᴏᴜʀ ᴘᴇʀꜱᴏɴᴀʟ ғɪʟᴇ ᴅᴇʟɪᴠᴇʀʏ ᴀꜱꜱɪꜱᴛᴀɴᴛ ⚡\nꜱʜᴀʀᴇ ꜰɪʟᴇꜱ ɪɴꜱᴛᴀɴᴛʟʏ\nɴᴏ ᴅᴇʟᴀʏ, ᴊᴜꜱᴛ ꜱᴘᴇᴇᴅ 🚀</b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<blockquote>ʜᴇʟʟᴏ {first} ✨</blockquote>\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ♻️ ᴛʀʏ ᴀɢᴀɪɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ 📥 ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>⚜️ 𝙿𝚘𝚜𝚝 𝚋𝚢 ~ 𝐌𝐎𝐕𝐈𝐄 𝐓𝐀𝐋𝐊</b>\n<b>⚡𝖩𝗈𝗂𝗇 Us ~ ❤️</b>\n<b>➦『 @movie_talk_backup 』</b>")  #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = False  # Button show hoga (disable nahi hoga)
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"
#--------------------------------------------


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
