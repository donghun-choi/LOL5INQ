from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
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
    # print('보낸 이 :',message.author)
    # print('내용 :', message.content)
    # print('시간 : ', )
    
    post = {
        "author":   str(message.author),
        "text":     str(message.content),
        "date":     str(datetime.now()), # => TODO : message에 과연 보낸 시간 등의 정보는 포함되지 않을까? 그럴리는 없을 것 같은데.. 수정해 봅시다
        }
    
    tcollection.insert_one(post).inserted_id
    
    
#TODO : 누가 봐도 개 #@$같이 짠 코드입니다. 빨리 고쳐야 함...

# 이 위는 싹 다 함수화 시키거나 나가 뒤지거나 둘중에 하나만 해줍시다.