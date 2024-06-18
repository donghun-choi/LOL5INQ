import discord
from utils import cohere_res
from utils import db_control
from .nlp import classifier
import os
class BotClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name="WWDC 2024"))
        print('Logged on as', self.user)

    async def on_message(self, message):
        db_control.add_chat_to_db(message)
        if classifier.good_to_answer(self,message):
            async with message.channel.typing(): # Key UI. 답변이 생성되는 사이에 봇이 입력중 . . . 띄움 => 어디에 입력중이 뜨는거지? 아마 답장하는 채널
                await message.channel.send(
                    cohere_res.get_response(
                        message.content,
                        preamble=os.getenv('main_t')
                        )
                    )
            return message
    intents = discord.Intents.default()
    intents.message_content = True


# TODO : 분활화 필요. discord bot control만 해야 하는데 이놈이 다 하고 있음. 전문가의 도음 필요..