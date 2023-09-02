from pyrogram.types import InlineKeyboardButton
from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3

def start_button(client):
    buttons = []

    if FORCE_SUB_CHANNEL:
        buttons.append([InlineKeyboardButton(text="Join Channel 1", url=client.invitelink)])
    
    if FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="Join Group", url=client.invitelink2)])

    if FORCE_SUB_CHANNEL2:
        buttons.append([InlineKeyboardButton(text="Join Channel 2", url=client.invitelink3)])

    if FORCE_SUB_CHANNEL3:
        buttons.append([InlineKeyboardButton(text="Join Channel 3", url=client.invitelink4)])

    buttons.append([InlineKeyboardButton(text="Help", callback_data="help")])
    buttons.append([InlineKeyboardButton(text="Close", callback_data="close")])

    return buttons

def fsub_button(client, message):
    buttons = []

    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="Join Channel 1", url=client.invitelink)])
        buttons.append([InlineKeyboardButton(text="Join Group", url=client.invitelink2)])
    
    if FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="Join Channel 2", url=client.invitelink3)])
    
    if FORCE_SUB_CHANNEL3 and FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="Join Channel 3", url=client.invitelink4)])

    try:
        buttons.append(
            [InlineKeyboardButton(
                text="Restart",
                url=f"https://t.me/{client.username}?start={message.command[1]}",
            )]
        )
    except IndexError:
        pass

    return buttons
