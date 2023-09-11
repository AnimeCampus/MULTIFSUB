import os
import sys
from os import environ, execle, system
from git import Repo
from git.exc import InvalidGitRepositoryError
from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot
from config import ADMINS, LOGGER

UPSTREAM_REPO = "https://github.com/PyroUserBot/MULTIFSUB"


def generate_changelog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    active_branch = repo.active_branch.name
    changelog = ""
    tldr_changelog = ""
    date_format = "%d/%m/%y || %H:%M"
    for commit in repo.iter_commits(diff):
        changelog += (
            f"\n\n💬 <b>{commit.count()}</b> 🗓 <b>[{commit.committed_datetime.strftime(date_format)}]</b>\n<b>"
            f"<a href={upstream_repo_url}/commit/{commit}>[{commit.summary}]</a></b> 👨‍💻 <code>{commit.author}</code>"
        )
        tldr_changelog += f"\n\n💬 {commit.count()} 🗓 [{commit.committed_datetime.strftime(date_format)}]\n[{commit.summary}] 👨‍💻 {commit.author}"
    if changelog:
        return str(f"<b>Updates for <a href={upstream_repo_url}/tree/{active_branch}>[{active_branch}]</a>:</b>" + changelog), str(f"Updates for {active_branch}:" + tldr_changelog)
    return changelog, tldr_changelog


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    active_branch = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_remote = repo.remote("upstream")
    else:
        ups_remote = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_remote.fetch(active_branch)
    changelog, tl_changelog = generate_changelog(repo, f"HEAD..upstream/{active_branch}")
    return bool(changelog)


@Bot.on_message(filters.command("update") & filters.user(ADMINS))
async def update_bot(_, message: Message):
    msg = await message.reply_text("Checking for updates...")
    update_available = updater()
    if update_available:
        await msg.edit("✅ Update finished!")
        system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
        execle(sys.executable, sys.executable, "main.py", environ)
        return
    await msg.edit(
        f"Bot is **up-to-date** with branch [master]({UPSTREAM_REPO}/tree/master)",
        disable_web_page_preview=True,
    )


@Bot.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply_text("`Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ Bot has restarted!\n\n")
    os.system(f"kill -9 {os.getpid()} && bash start")
