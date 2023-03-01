# -*- coding: utf-8 -*-
import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


token = 'your_token'  # e.g.'8e81b593e23497d1546f9b9dc45c0013f55ac67ec051a6ab15457eabe232f0f3ba6f4876790d868b2fe3e'
version = 'your_version'  # 5.103
domain = 'your_domain'  #'legion_damned'
group_id = 'your_group_id_vk'  # 120667630

print('Start Bot')

vk_session = vk_api.VkApi(token=token, scope='your_scope')   # e.g. 140488159

session_api = vk_session.get_api()

