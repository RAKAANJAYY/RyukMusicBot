# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME
from handlers.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🕊️ command dasar untuk bot</b>
**[ GROUP SETTINGS ]
/play (title) - play music via YouTube
/ytp (title) - play music live
/stream (reply to audio) - play music via reply to audio
/playlist - view queue list
/song (title) - download music from YouTube
/video (title) - download videos from YouTube
/lyrics - (title) search for lyrics
[ CHANNEL SETTINGS ]
/cplay - play music via channel
/cplayer - view queue list
/cpause - pause music player
/cresume - resume music playing
/cskip - skip to next song
/cend - stops music
/admincache - refresh admin cache
/ubjoinc - invites assistants to join the channel

𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 @KGSupportgroup**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⟪", callback_data="cbguide"
                    ),
                    InlineKeyboardButton(
                        "⟫", callback_data="cbadvanced"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🕊️ command lanjutan</b>

**/start (in group) - see alive bot
/reload - update bot and refresh admin list
/cache - cache admin cache
/ping - check bot ping

𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 @KGSupportgroup**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⟪", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "⟫", callback_data="cbadmin"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🕊️ command untuk admin grup</b>

**/player - view playback status
/pause - pauses playing music
/resume - resume paused music
/skip - skip to next song
/end - mute the music
/userbotjoin - invites assistants to join the group
/musicplayer (on / off) - turn off / on the music player in your group

𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 @KGSupportgroup**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⟪", callback_data="cbadvanced"
                    ),
                    InlineKeyboardButton(
                        "⟫", callback_data="cbsudo"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🕊️ command untuk sudo</b>

**/player - view playback status
/pause - pauses music playback
/resume - resume paused music
/skip - skip to next song
/end - mute the music
/userbotjoin - invites assistants to join the group
/musicplayer (on/off) - turn off/on music player in your group
𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 @KGSupportgroup**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⟪", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "⟫", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🕊️ Command fun</b>

**/chika - cek sendiri
/wibu - cek sendiri
/asupan - cek sendiri
/truth - cek sendiri
/dare - cek sendiri

𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 @KGSupportgroup**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⟪", callback_data="cbsudo"
                    ),
                    InlineKeyboardButton(
                        "ᴄʟᴏsᴇ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""CARA MENGGUNAKAN BOT INI :

**1.) First, add it to your group.
2.) Then make admin with all permissions except anonymous admin.
3.) Add @{ASSISTANT_NAME} to your group or you can type `/userbotjoin` to invite assistant.
4.) Turn on voice chat first before playing music.

𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 @KGSupportgroup**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄᴏᴍᴍᴀɴᴅs", callback_data="cbbasic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ᴄʟᴏsᴇ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
