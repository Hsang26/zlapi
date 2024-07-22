from zlapi.simple import ZaloAPI
from zlapi.models import *

imei = ""
session_cookies = {}
bot = ZaloAPI(
	"</>", "</>",
	imei=imei,
	session_cookies=session_cookies,
	prefix="."
)


@bot.events
async def on_listening():
	print("Bot is ready.")


@bot.events
async def on_message(ctx):
	await bot.mark_as_delivered(ctx)
	await bot.mark_as_read(ctx)


@bot.register_handler(commands=["groupid", "gid"])
async def test(ctx):
	message = f"This group's ID is:\n{ctx.thread_id}"
	style = MultiMsgStyle([
		MessageStyle(offset=0, length=19, style="bold", auto_format=False),
		MessageStyle(offset=20, length=len(ctx.thread_id), style="color", color="#bac2de", auto_format=False),
		MessageStyle(offset=20, length=len(ctx.thread_id), style="font", size="14", auto_format=False)
	])
	
	await bot.reply_message(Message(text=message, style=style), ctx.message_object, ctx.thread_id, ctx.thread_type)


bot.listen()
	