from utils import cohere_res
import os

def is_not_for_me(message):
    # print(os.getenv('isthisforme_t'))
    print(cohere_res.get_response(
        message,
        model='command',
        preamble=os.getenv('isthisforme_t_e'),
        # model='command-r'
        )
    )
    return 1

def is_nsfw(message):
    return cohere_res.response(
        message,
        preamble=os.getenv('nsfw_t'))


def good_to_answer(self,message):
    # if message.channel.id!=int(os.getenv('CHANNEL_5INQ')):
        # return
    if message.author == self.user:
        return
    
    # if message.
    
    # isnotforme = int(is_not_for_me(message.content))
    # print('나에게 온 메세지가 아니다 :',isnotforme)
    
    # if isnotforme:
        # return
    # if isnsfw(message.content):
        # return
    
    return 1


# 자체 모델로 전환 시급. 비용을 많이 아낄 수 있을 것...... => 아닌가?