from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3
from pyrogram.types import InlineKeyboardButton

def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="😙Hᴇᴋᴘ😙", callback_data="help"),
                InlineKeyboardButton(text="🍁Cʟᴏsᴇ🍁", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🦁Gʀᴏᴜᴘ🦁", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="😙Hᴇʟᴘ😙", callback_data="help"),
                InlineKeyboardButton(text="🍁Cʟᴏsᴇ🍁", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="👾Hᴇʟᴘ👾", callback_data="help"),
                InlineKeyboardButton(text="🍁Cʟᴏsᴇ🍁", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Help", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟸", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="🍁Cʟᴏsᴇ🍁", callback_data="close")],
        ]
        return buttons
    # Add two more conditions here
    if FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟹", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="👾Hᴇʟᴘ👾", callback_data="help"),
                InlineKeyboardButton(text="🍁Cʟᴏsᴇ🍁", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL3 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟼", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="😙Hᴇʟᴘ😙", callback_data="help"),
                InlineKeyboardButton(text="🍁Cʟᴏsᴇ🍁", callback_data="close"),
            ],
        ]
        return buttons

def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟸", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ʀᴇsᴛᴀʀᴛ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ʀᴇsᴛᴀʀᴛ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟸", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ʀᴇsᴛᴀʀᴛ ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    # Add two more conditions here
    if FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟹", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ʀᴇsᴛᴀʀᴛ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL3 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟺", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ʀᴇsᴛᴀʀᴛ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
