import discord
from utils import db_control
from .nlp import classifier
from utils import history_cohere
import os
class BotClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name="WWDC 1983"))
        print('Logged on as', self.user)

    async def on_message(self, message):
        if classifier.good_to_answer(self,message):
            async with message.channel.typing():
                history = db_control.get_history(message.author)
                response_text=history_cohere.get_response(
                            message.content,
                            preamble=os.getenv('main_t'),
                            chat_hisory=history
                            )
                await message.channel.send(response_text)
                db_control.add_chat_to_db(message,response_text)
    intents = discord.Intents.default()
    intents.message_content = True