import discord
import vk
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from datetime import datetime


client = discord.Client()
chan = []

vk_session = vk.vk_session
group_id = vk.group_id

longpoll = VkBotLongPoll(vk_session, group_id, wait=25) #ошибка на этой строке


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global chan
    if message.author == client.user:
        return

    if message.content.startswith('$start'):
        await message.channel.send('Reading the wall!')
        chan = message.channel
        while longpoll.listen():
            if longpoll.listen():
                print(longpoll.listen(), 'listening...')
                check = longpoll.check()
                if check != []:
                    type = check[0].raw['type']
                    print(type, 'second')
                    if type == 'wall_post_new':
                        print('sending message')
                        print(check[0].raw['object']['text'], check[0].raw['object']['attachments'][0]['photo']['sizes'][5]['url'],  'first time')
                        text = check[0].raw['object']['text']
                        date = check[0].raw['object']['date']
                        dt = str(datetime.fromtimestamp(date))
                        photo = []
                        att = check[0].raw['object']['attachments']
                        presend = ''
                        for i in att:
                            photo = i['photo']['sizes'][5]['url']
                            presend = presend + str(photo) + '\n'
                        await chan.send('New post' + ', '+ dt + '\n' + text + '\n' + presend)

# retrieve your token to run first e.g. 'NjU5Nzg5ODcxNjE5MjQ0MDQy.Xhi21Q.mnYEKKCyKgPmkEKsnU-SRwSZSxc'
client.run('your_token)
