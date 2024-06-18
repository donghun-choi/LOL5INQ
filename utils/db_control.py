from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import pytz
from dotenv import load_dotenv
from datetime import datetime
load_dotenv(verbose=True)

uri = f"mongodb+srv://{os.getenv('MONGODB_UNAME')}:{os.getenv('MONGODB_PW')}@{os.getenv('MONGODB_DB')}"
client = MongoClient(uri, server_api=ServerApi('1'))

today = datetime.today()
day = f"{today.year % 100}_{today.month:02d}_{today.day:02d}"
print(day)

tcollection = client['chat'][day]


def add_chat_to_db(message:any): # #TODO : 함수명 구려요
    post = {
        "author":   str(message.author),
        "text":     str(message.content),
        "date":     str(CvtToLocalTime(message.created_at)), #=> 깔끔한 구현이라고는 안 하겠으나, 쩔 수 없음.
        }
    tcollection.insert_one(post).inserted_id #TODO : Sohould be fixed


def CvtToLocalTime(input_utc_time_str):
  kst_time = input_utc_time_str.astimezone(pytz.timezone('Asia/Seoul'))
  return kst_time.strftime("%Y-%m-%d %H:%M:%S.%f")

#TODO : 누가 봐도 개 #@$같이 짠 코드입니다. 빨리 고쳐야 함...

# 이 위는 싹 다 함수화 시키거나 나가 뒤지거나 둘중에 하나만 해줍시다.