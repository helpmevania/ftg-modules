from .. import loader, utils
import asyncio
import telethon

@loader.tds
class NoTagsMod(loader.Module):
    """Не тегайте меня!"""
    strings = {"name":"NoTags",
    "args": "🦊 <b>Incorrect args specified</b>", 
    "on": "🦊 <b>Now I ignore tags in this chat</b>",
    "off": "🦊 <b>Now I don't ignore tags in this chat</b>",
    "on_strict": "🦊 <b>Now I automatically read messages in this chat</b>",
    "off_strict": "🦊 <b>Now I don't automatically read messages in this chat</b>",
    "do_not_tag_me": "🦊 <b>Please, do not tag me.</b>"}

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def fucktagscmd(self, message):
        """.fucktags <chat|optional> - Включить \\ выключить возможность тегать вас"""
        args = utils.get_args_raw(message)
        try:
            cid = (await self.client.get_entity(args)).id
        except:
            cid = utils.get_chat_id(message)

        if cid not in self.db.get('FuckTags', 'tags', []):
            self.db.set('FuckTags', 'tags', self.db.get('FuckTags', 'tags', []) + [cid])
            await utils.answer(message, self.strings('on', message))
        else:
            self.db.set('FuckTags', 'tags', list(set(self.db.get('FuckTags', 'tags', [])) - set([cid])))
            await utils.answer(message, self.strings('off', message))

    async def fuckallcmd(self, message):
        """.fuckall <chat|optional> - Включить \\ выключить режим авточтения в чате"""
        args = utils.get_args_raw(message)
        try:
            cid = (await self.client.get_entity(args)).id
        except:
            cid = utils.get_chat_id(message)

        if cid not in self.db.get('FuckTags', 'strict', []):
            self.db.set('FuckTags', 'strict', self.db.get('FuckTags', 'strict', []) + [cid])
            await utils.answer(message, self.strings('on_strict', message))
        else:
            self.db.set('FuckTags', 'strict', list(set(self.db.get('FuckTags', 'strict', [])) - set([cid])))
            await utils.answer(message, self.strings('off_strict', message))

    async def watcher(self, message):
        if utils.get_chat_id(message) in self.db.get('FuckTags', 'tags', []) and message.mentioned:
            await self.client.send_read_acknowledge(message.chat_id, message, clear_mentions=True)
            await utils.answer(message, self.strings('do_not_tag_me', message))
        elif utils.get_chat_id(message) in self.db.get('FuckTags', 'strict', []):
            await self.client.send_read_acknowledge(message.chat_id, message)

