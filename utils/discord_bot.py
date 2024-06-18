import discord
from utils import cohere_res
from utils.db_control import add_chat_to_db
from .nlp import classifier
import os
testmode = 0

class BotClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name="2024 LoL Champions Korea Summer"))
        print('Logged on as', self.user)

    async def on_message(self, message):
        add_chat_to_db(message)
        # if classifier.good_to_answer(self,message):
        #     async with message.channel.typing(): # Key UI. 답변이 생성되는 사이에 봇이 입력중 . . . 띄움 => 어디에 입력중이 뜨는거지?
        #         await message.channel.send(
        #             cohere_res.get_response(
        #                 message.content,
        #                 preamble=os.getenv('main_t')
        #                 )
        #             )
        #     return message
intents = discord.Intents.default()
intents.message_content = True


# TODO : 분활화 필요. discord bot control만 해야 하는데 이놈이 다 하고 있음. 전문가의 도음 필요..