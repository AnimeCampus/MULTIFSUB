# (©)Codexbotz
# Recoded by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_CHANNEL,
    FORCE_SUB_GROUP,
    FORCE_SUB_CHANNEL2,
    FORCE_SUB_CHANNEL3,
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
            bot_me = await self.get_me()
            self.username = bot_me.username
            self.bot_name = bot_me.first_name
            self.LOGGER(__name__).info(
                f"TG_BOT_TOKEN detected!\n┌ First Name: {self.bot_name}\n└ Username: @{self.username}\n——"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).info(
                "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
            )
            sys.exit()

        if FORCE_SUB_CHANNEL:
            try:
                channel_info = await self.get_chat(FORCE_SUB_CHANNEL)
                invite_link = channel_info.invite_link
                if not invite_link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    invite_link = channel_info.invite_link
                self.invite_link = invite_link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_CHANNEL detected!\n┌ Title: {channel_info.title}\n└ Chat ID: {channel_info.id}\n——"
                )
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning(
                    "Bot couldn't fetch the invite link for FORCE_SUB_CHANNEL!"
                )
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} is an admin in the specified channel. Current F-Subs Channel ID: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
                )
                sys.exit()

        if FORCE_SUB_GROUP:
            try:
                group_info = await self.get_chat(FORCE_SUB_GROUP)
                invite_link = group_info.invite_link
                if not invite_link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP)
                    invite_link = group_info.invite_link
                self.invite_link2 = invite_link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_GROUP detected!\n┌ Title: {group_info.title}\n└ Chat ID: {group_info.id}\n——"
                )
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning(
                    "Bot couldn't fetch the invite link for FORCE_SUB_GROUP!"
                )
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} is an admin in the specified group. Current F-Subs Group ID: {FORCE_SUB_GROUP}"
                )
                self.LOGGER(__name__).info(
                    "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
                )
                sys.exit()

        # Add conditions and logger messages for FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3
        if FORCE_SUB_CHANNEL2:
            try:
                channel_info2 = await self.get_chat(FORCE_SUB_CHANNEL2)
                invite_link2 = channel_info2.invite_link
                if not invite_link2:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                    invite_link2 = channel_info2.invite_link
                self.invite_link2 = invite_link2
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_CHANNEL2 detected!\n┌ Title: {channel_info2.title}\n└ Chat ID: {channel_info2.id}\n——"
                )
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning(
                    "Bot couldn't fetch the invite link for FORCE_SUB_CHANNEL2!"
                )
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} is an admin in the specified channel. Current F-Subs Channel2 ID: {FORCE_SUB_CHANNEL2}"
                )
                self.LOGGER(__name__).info(
                    "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
                )
                sys.exit()

        if FORCE_SUB_CHANNEL3:
            try:
                channel_info3 = await self.get_chat(FORCE_SUB_CHANNEL3)
                invite_link3 = channel_info3.invite_link
                if not invite_link3:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL3)
                    invite_link3 = channel_info3.invite_link
                self.invite_link3 = invite_link3
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_CHANNEL3 detected!\n┌ Title: {channel_info3.title}\n└ Chat ID: {channel_info3.id}\n——"
                )
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning(
                    "Bot couldn't fetch the invite link for FORCE_SUB_CHANNEL3!"
                )
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} is an admin in the specified channel. Current F-Subs Channel3 ID: {FORCE_SUB_CHANNEL3}"
                )
                self.LOGGER(__name__).info(
                    "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test_message = await self.send_message(chat_id=db_channel.id, text="Test Message", disable_notification=True)
            await test_message.delete()
            self.LOGGER(__name__).info(
                f"CHANNEL_ID Database detected!\n┌ Title: {db_channel.title}\n└ Chat ID: {db_channel.id}\n——"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Make sure @{self.username} is an admin in your database channel. Current CHANNEL_ID: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "Bot stopped. Join the group https://t.me/SharingUserbot for assistance."
            )
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"[🔥 SUCCESSFULLY ACTIVATED! 🔥]\n\nBOT Created by @{OWNER}\nIf @{OWNER} needs assistance, please ask in the group https://t.me/SharingUserbot"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
