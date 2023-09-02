# (©)Codexbotz
# Recoded by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import os
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_CHANNEL,
    FORCE_SUB_CHANNEL2,
    FORCE_SUB_CHANNEL3,
    FORCE_SUB_GROUP,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.LOGGER(__name__).info(
                f"TG_BOT_TOKEN detected!\n┌ First Name: {self.namebot}\n└ Username: @{self.username}\n——"
            )
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
            )
            sys.exit()

        if FORCE_SUB_CHANNEL:
            try:
                info = await self.get_chat(FORCE_SUB_CHANNEL)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = info.invite_link
                self.invitelink = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_CHANNEL detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot couldn't fetch the invite link for FORCE_SUB_CHANNEL!"
                )
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} is an admin in that channel. Current Channel ID for F-Subs Channel: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
                )
                sys.exit()

        if FORCE_SUB_CHANNEL2:
            try:
                info = await self.get_chat(FORCE_SUB_CHANNEL2)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                    link = info.invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_CHANNEL2 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot couldn't fetch the invite link for FORCE_SUB_CHANNEL2!"
                )
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} is an admin in that channel. Current Channel ID for F-Subs Channel 2: {FORCE_SUB_CHANNEL2}"
                )
                self.LOGGER(__name__).info(
                    "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
                )
                sys.exit()

        if FORCE_SUB_CHANNEL3:
            try:
                info = await self.get_chat(FORCE_SUB_CHANNEL3)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL3)
                    link = info.invite_link
                self.invitelink3 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_CHANNEL3 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot couldn't fetch the invite link for FORCE_SUB_CHANNEL3!"
                )
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} is an admin in that channel. Current Channel ID for F-Subs Channel 3: {FORCE_SUB_CHANNEL3}"
                )
                self.LOGGER(__name__).info(
                    "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
                )
                sys.exit()

        if FORCE_SUB_GROUP:
            try:
                info = await self.get_chat(FORCE_SUB_GROUP)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP)
                    link = info.invite_link
                self.invitelink_group = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_GROUP detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot couldn't fetch the invite link for FORCE_SUB_GROUP!"
                )
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} is an admin in that group. Current Group ID for F-Subs Group: {FORCE_SUB_GROUP}"
                )
                self.LOGGER(__name__).info(
                    "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
                )
                sys.exit()

        # Rest of the code...

if __name__ == "__main__":
    Bot().run()
