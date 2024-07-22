from zlapi.Async import ZaloAPI
from zlapi.models import *


class VrxxBot(ZaloAPI):
	async def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type):
		if not isinstance(message, str):
			return
		
		if author_id != client.uid:
			message = Message(text=message)
			await self.send(message, thread_id, thread_type)



imei = ""
session_cookies = {}
client = VrxxBot("</>", "</>", imei=imei, session_cookies=session_cookies)
client.listen()