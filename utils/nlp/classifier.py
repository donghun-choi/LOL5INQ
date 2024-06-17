from utils import cohere_res
import os

def notforme(message):
    # print(os.getenv('isthisforme_t'))
    return cohere_res.response(
        message,
        preamble=os.getenv('isthisforme_t'),
        # model='command-r'
        )

def isnsfw(message):
    return cohere_res.response(
        message,
        preamble=os.getenv('nsfw_t'))


def good_to_answer(self,message):
    if message.channel.id!=1184539017241440396:
        return
    if message.author == self.user:
        return
    
    # if message.
    
    # isnotforme = int(notforme(message.content))
    # print('나에게 온 메세지가 아니다 :',isnotforme)
    
    # if isnotforme:
        # return
    # if isnsfw(message.content):
        # return
    
    return 1