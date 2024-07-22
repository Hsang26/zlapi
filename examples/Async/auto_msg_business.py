from zlapi.Async import ZaloAPI
from zlapi.models import *


class VrxxBot(ZaloAPI):
	async def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type):
		if not isinstance(message, str):
			return
		
		if author_id != client.uid and thread_type == ThreadType.USER:
			msg = "🤖 Tin nhắn tự động\n| Hiện tại tôi đang bận và không thể rep tin nhắn, hãy thử lại sau!"
			style = MultiMsgStyle([
				MessageStyle(offset=0, length=20, style="font", size="12", auto_format=False),
				MessageStyle(offset=3, length=17, style="color", color="#89dceb", auto_format=False),
				MessageStyle(offset=20, length=1, style="color", color="#585b70", auto_format=False),
				MessageStyle(offset=20, length=1, style="bold", auto_format=False),
				MessageStyle(offset=22, length=len(msg.encode()), style="font", size="13", auto_format=False),
				MessageStyle(offset=22, length=len(msg.encode()), style="color", color="#cdd6f4", auto_format=False)
			])
			msg = Message(text=msg, style=style)
			await self.send(msg, thread_id, thread_type)



imei = ""
session_cookies = {}
client = VrxxBot("</>", "</>", imei=imei, session_cookies=session_cookies)
client.listen()