@bot.on(admin_cmd(pattern="repo"))
@bot.on(sudo_cmd(pattern="repo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    Repo = f"[Click Here](https://github.com/RDXBOT/RDXSPAMBOT)"
    Deploy = f"[Click Here]https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FRDXBOT%2FRDXSPAMBOT)"
    await edit_or_reply(
        event, f"**RDX SPAM BOT:** {Repo}\n\n**Deploy Now:** {Deploy}"
    )
