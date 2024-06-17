from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv(verbose=True)

uri = f"mongodb+srv://choidonghun:{os.getenv('MONGODBPW')}@chats.9uyaxhm.mongodb.net/?retryWrites=true&w=majority&appName=chats"
client = MongoClient(uri, server_api=ServerApi('1'))

today = datetime.today()
day = f"{today.year % 100}_{today.month:02d}_{today.day:02d}"
print(day)

tcollection = client['chat'][day]


def add_chat_to_db(information):
    # print('보낸 이 :',information.author)
    # print('내용 :', information.content)
    # print('시간 : ', )
    
    post = {
        "author": str(information.author),
        "text": str(information.content),
        "date": str(datetime.now()),
        }
    
    tcollection.insert_one(post).inserted_id