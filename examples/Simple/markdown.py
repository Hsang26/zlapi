from zlapi.simple import ZaloAPI
from zlapi.models import *

imei = ""
session_cookies = {}
bot = ZaloAPI(
	"</>", "</>",
	prefix=".",
	imei=imei,
	session_cookies=session_cookies
)

# CUSTOM EVENTS
@bot.events
async def on_message_delivered(ctx):
	pass


@bot.events
async def on_marked_seen(ctx):
	pass


@bot.events
async def on_listening():
	print("Bot is ready.")


@bot.events
async def on_message(ctx):
	await bot.mark_as_delivered(ctx)
	await bot.mark_as_read(ctx)

# END CUSTOM EVENTS


@bot.register_handler(message = lambda x: x[:8] == "markdown")
async def markdown(ctx):
	message = ctx.message[8:]
	message = Message(text=message, parse_mode="Markdown")
	
	await bot.send_message(message, ctx.thread_id, ctx.thread_type)


@bot.register_handler(message = lambda x: x[:4] == "html")
async def markdown_html(ctx):
	message = ctx.message[4:]
	message = Message(text=message, parse_mode="HTML")
	
	await bot.send_message(message, ctx.thread_id, ctx.thread_type)


bot.listen()	