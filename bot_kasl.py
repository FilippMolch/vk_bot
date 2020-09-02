import vk_api
import time
import datetime
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests, dpath.util

def write_msg(message):
    vk.method('messages.send', {'peer_id': event.object.peer_id, 'message': message, 'random_id': 0})

token = ""
vk = vk_api.VkApi(token=token)
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, 190986135)
#MESSAGES = 2**12
#vk_api.VkUserPermissions(MESSAGES)
try:
    for event in longpoll.listen():
        print(event)
        request = event.object.text
        if event.type == VkBotEventType.MESSAGE_NEW:
            if request == '/hello':
                write_msg('ага, дарова')

except Exception as E:
    print(Exception)
