import random
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message
from telethon import events
from asyncio import sleep

@loader.tds
class FrogMod(loader.Module):
    """Frog"""
    strings = {'name': 'helpmv'}

    async def watcher(self, message):
        if message.sender_id in {1568736811}:
            if "Реанимируй" in message.message:
                await sleep(10)
                await message.respond('реанимировать жабу')
        try:
            chat = message.chat_id
            me = await message.client.get_me()
            name = me.first_name

            BK = None
            EK = {
                -1001363387233
            }

            if message.sender_id in {1568736811}:
                BK = {-1001363387233}
            if message.sender_id in {1568736811}:
                BK = {
                    -1001363387233,
                }

            if message.sender_id in {1568736811}:
                BK = {-1001363387233}

            KW = {-1001363387233}

            if message.sender_id in {1568736811}:
                if "Моя жаба" in message.message:
                    randelta = random.randint(55, 75)
                    async with message.client.conversation(chat) as conv:
                        try:
                            response = conv.wait_event(events.NewMessage(incoming=True, from_users=1744359315, chats=message.chat_id))
                            await sleep (10)
                            await message.client.send_message(chat, 'жаба инфо')
                            response = await response                                                     

                            if "(Можно откормить)" in response.text:
                                if message.chat_id in EK:
                                    delta = timedelta(hours=4, seconds=randelta)
                                    delta_r = timedelta(hours=4, seconds=10)
                                    await sleep(10)
                                    await message.respond('покормить жабу')
                                    await message.client.send_message(chat, 'покормить жабу', schedule=delta_r)
                                    await message.client.send_message(chat, 'Моя жаба', schedule=delta)
                                else:
                                    if "Жабу можно покормить" in response.text:
                                        delta = timedelta(hours=12, seconds=randelta)
                                        delta_r = timedelta(hours=12, seconds=10)
                                        await sleep(10)
                                        await message.respond('покормить жабу')
                                        await message.client.send_message(chat, 'Покормить жабу', schedule=delta_r)
                                        await message.client.send_message(chat, 'Моя жаба', schedule=delta)

                            if "Жабу можно отправить" in response.text:
                                delta = timedelta(hours=2, seconds=randelta)
                                delta_r = timedelta(hours=2, seconds=10)
                                if message.chat_id in EK:
                                    if "В подземелье можно через 2ч" in response.text:
                                        await sleep(10)
                                        await message.respond('реанимировать жабу')
                                        await sleep(10)
                                        await message.respond('работа грабитель')
                                        await message.client.send_message(chat, 'Завершить работу', schedule=delta_r)
                                        await message.client.send_message(chat, 'Моя жаба', schedule=delta)
                                else:
                                    await sleep(10)
                                    await message.respond('реанимировать жабу')
                                    await sleep(10)
                                    await message.respond('работа грабитель')
                                    await message.client.send_message(chat, 'Завершить работу', schedule=delta_r)
                                    await message.client.send_message(chat, 'Моя жаба', schedule=delta)

                            if "Можно забрать" in response.text:
                                delta = timedelta(hours=6, seconds=randelta)
                                delta_m = timedelta(seconds=randelta)
                                await sleep(10)
                                await message.respond('завершить работу')
                                await message.client.send_message(chat, 'поход в столовую', schedule=delta)
                                await message.client.send_message(chat, 'Моя жаба', schedule=delta_m)
                                if message.chat_id not in {-1001363387233}:
                                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1568736811, chats=message.chat_id))
                                    await sleep (10)
                                    await message.client.send_message(chat, 'война')
                                    response = await response

                                    if "⚔️Состояние⚔️: Не" in response.text:
                                        if message.chat_id in KW:
                                            await sleep(10)
                                            await message.respond('начать')
                                    if name + " | Не атаковал" in response.text:
                                        await sleep(10)
                                        await message.respond('реанимировать жабу')
                                        await sleep(10)
                                        await message.respond('напасть')

                            if "Можно отправиться" in response.text:
                                if message.chat_id in EK:
                                    await sleep(10)
                                    await message.respond('реанимировать жабу')
                                    await sleep(10)
                                    await message.respond('отправиться в золотое подземелье')
                                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1568736811, chats=message.chat_id))
                                    await sleep (10)
                                    await message.client.send_message(chat, 'мое снаряжение')
                                    response = await response
                                    if "🗡Ближний бой: Отсутствует" in response.text:
                                        await sleep(10)
                                        await message.respond('скрафтить клюв цапли')
                                    if "🏹Дальний бой: Отсутствует" in response.text:
                                        await sleep(20)
                                        await message.respond('скрафтить букашкомет')
                                    if "🐸Наголовник: Отсутствует" in response.text:
                                        await sleep(30)
                                        await message.respond('скрафтить наголовник из клюва цапли')
                                    if "🥼Нагрудник: Отсутствует" in response.text:
                                        await sleep(40)
                                        await message.respond('скрафтить нагрудник из клюва цапли')
                                    if "👞Налапники: Отсутствует" in response.text:
                                        await sleep(50)
                                        await message.respond('скрафтить налапники из клюва цапли')
                                    if "🏋️‍♀️Банда: Отсутствует" in response.text:
                                        await sleep(60)
                                        await message.respond('собрать банду')

                                if message.chat_id in KW:
                                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1568736811, chats=message.chat_id))
                                    await sleep (10)
                                    await message.client.send_message(chat, 'мой')
                                    response = await response
                                    if "Клан" in response.text:
                                        if "🕒Пойти" not in response.text:
                                            await sleep (10)
                                            await message.respond('отправиться за картой')
                                            await sleep (20)
                                            await message.respond('отправиться за картой')
                        except: pass

            if message.sender_id in {1568736811}:
                randelta = random.randint(6, 9)
                delta = timedelta(minutes=randelta)
                if "Сейчас выбирает ход: " + name in message.message:
                    await message.click(0)
                if "help me i am Vanya " + name in message.message:
                    await sleep (10)
                    await message.respond('реанимировать жабу')
                    await sleep (10)
                    await message.respond('отправиться за картой')
                if "Тебе жаба, Милая Беседа" in message.message:
                    await message.client.send_message(chat, 'Моя жаба', schedule=delta)

            if message.sender_id in {1568736811}:
                if "Жабу на тусу" in message.message:
                    await sleep(20)
                    await message.respond('завершить работу')
                    await sleep(30)
                    await message.respond('реанимировать жабу')
                    await sleep(35)
                    await message.respond('жабу на тусу')
                if "Кл" in message.message:
                    await message.respond('твп')
                if "Отпй" in message.message:
                    await message.respond('жарк')
                if "Нн" in message.message:
                    await sleep(55)
                    await message.respond('реанимировать жабу')
                    await sleep(55)
                    await message.respond('напасть на клан')           
                if "завершить работу" in message.message:
                    await sleep(5)
                    await message.respond('завершить работу')
                if "работа крупье" in message.message:
                    await sleep(10)
                    await message.respond('работа крупье')
                if "работа грабитель" in message.message:
                    await sleep(5)
                    await message.respond('работа грабитель')
                if "@tgtoadbot покормить жабу" in message.message:
                    await sleep(20)
                    await message.respond('покормить жабу')
                if "покормить жабу" in message.message:
                    await sleep(20)
                    await message.respond('покормить жабу')
                if "Букашки 300" in message.message:
                    await sleep(5)
                    await message.reply('отправить букашки 300')
                if "Букашки 200" in message.message:
                    await sleep(5)
                    await message.reply('отправить букашки 200')
                if "Букашки 100" in message.message:
                    await sleep(10)
                    await message.reply('отправить букашки 100')
                if "Жаба" in message.message:
                    await sleep(10)
                    await message.respond('моя жаба')

            if message.chat_id in BK:
                if "хуила аптеки" in message.message:
                    await message.reply('отправить аптечки 5')
                if "хуила букашки" in message.message:
                    await message.reply('отправить букашки 500')
                if "гони леденцы" in message.message:
                    await message.reply('отправить леденцы 5')

            if message.sender_id in {1568736811}:
                if "Букашки сюда" in message.message:
                    await sleep(10)
                    await message.reply('отправить букашки 700')
                    await sleep(15)
                    await message.reply('отправить букашки 500')
                    await sleep(20)
                    await message.reply('отправить букашки 200')
                    await sleep(55)
                    await message.reply('отправить букашки 100')
                if "Леденцы мне😊" in message.message:
                    await sleep(55)
                    await message.reply('отправить леденцы 15')
                    await sleep(55)
                    await message.reply('отправить леденцы 10')
                    await sleep(55)
                    await message.reply('отправить леденцы 5')
        except:
            pass
