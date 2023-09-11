from pyrogram.types import InlineKeyboardButton
from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3

def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Donate", callback_data="help"),
                InlineKeyboardButton(text="Close ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="Group", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="Donate", callback_data="help"),
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="Channel", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="Donate", callback_data="help"),
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="Donate", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="Channel 1", url=client.invitelink),
                InlineKeyboardButton(text="Channel 2", url=client.invitelink2),
                InlineKeyboardButton(text="Channel 3", url=client.invitelink3),
                InlineKeyboardButton(text="Channel 4", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="Close", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Join Channel 2", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Restart",
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
                InlineKeyboardButton(text="Channel 1", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Restart",
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
                InlineKeyboardButton(text="Channel 1", url=client.invitelink),
                InlineKeyboardButton(text="Channel 2", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Restart ",
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
                InlineKeyboardButton(text="Channel 1", url=client.invitelink3),
            ],
        ]        
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Restart",
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
                InlineKeyboardButton(text="Channel 1", url=client.invitelink),
                InlineKeyboardButton(text="Channel 2", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Restart ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="Channel 1", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Restart",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="Channel 1", url=client.invitelink3),
                InlineKeyboardButton(text="Channel 2", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Restart ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
        
