# -*- coding: utf-8 -*-
import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


token = '8e81b593e23497d1546f9b9dc45c0013f55ac67ec051a6ab15457eabe232f0f3ba6f4876790d868b2fe3e'
version = 5.103
domain = 'legion_damned'
group_id = 120667630

print('Start Bot')

vk_session = vk_api.VkApi(token=token, scope=140488159)

session_api = vk_session.get_api()

