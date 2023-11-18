from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from defunc import *
import time
import random
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError


api_id = input('Введите ваш API ID телеграмма')
api_hash = input('Введите ваш API HASH телеграмма')
client0 = TelegramClient('client0', api_id, api_hash).start()

selection = int(input('[1] Парсинг\n[2] Инвайтинг\nВвод: '))
if selection == 1:

    chats = []
    last_date = None    
    size_chats = 200
    groups = []         

    result = client0(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=size_chats,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup is True:
                groups.append(chat)         
        except:
            continue

    i = 0
    print('Очистка базы юзернеймов: -1') 
    print('-----------------------------')
    for g in groups:
        print(str(i) + ' - ' + g.title)
        i+=1
    print('||[' + str(i + 1) + ' - ' + 'Спарсить всё' + ']||')
    g_index = int(input())

    print('Парсим!')
    if g_index < i + 1:
        target_group = groups[g_index]
        parsing(client0, target_group)
        print('Спарсино.')
    elif g_index == i + 1:
        for g_index in groups:
            parsing(client0, g_index)
        print('Было трудно, но мы справились)')
    elif g_index == 1234:
        f = open('participants.txt', 'w')
        f.close()
        print('Очистка выполнена успешно.')

elif selection == 2:
    with open('participants.txt', 'r') as f:
        users = list(f)
        
    channelname = input('Введите имя канала для инвайта (без "@")')
    for limit in range(20):
        try:
            inviting(client0, channelname, users[limit].replace('\n', ''))
            print(users[limit].replace('\n', ''))
            time.sleep(random.randrange(15, 40))
        except UserPrivacyRestrictedError:
            print('Пользователь ' + users[limit].replace('\n', '') + ' запретил его инвайтить. Пропускаем :(')
        except PeerFloodError:
            print('Телеграмм заспамлен. Сворачиваемся.')
            break
        except Exception as error:
            print(error)
            break
