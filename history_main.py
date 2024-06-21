from utils import history_discord_bot
from dotenv import load_dotenv
load_dotenv(verbose=True)
import os


#discord
discord_client = history_discord_bot.BotClient(intents=history_discord_bot.BotClient.intents)
discord_client.run(token=os.getenv('DISCORD_TOKEN'))

#TODO => Undefined. 할게 너무 많다.