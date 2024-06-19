import cohere
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

co = cohere.Client(os.getenv('COHERE_TOKEN'))

def get_response(
            message           :str,
            chat_hisory       :list   = None,
            preamble          :str    = None,
            model             :str    = 'command-r-plus', #=> may i serve another 싼 모델 내놔 시발
            temperature       :float  = 0.2,
            max_tokens        :int    = 128, #TODO => can be flexible with Input Length!!
            presence_penalty  :float  = 0.1
            ):
        
    response = co.chat(
            message           = message,
            chat_history      = chat_hisory,
            preamble          = preamble,
            model             = model,
            temperature       = temperature,
            max_tokens        = max_tokens,
            presence_penalty  = presence_penalty
    )
    return response.text #TODO: 다른 정보도 쓰자

chat_history = [
        
        {"role": "USER", "text": "최둥훈 알아?"},
        {"role": "CHATBOT", "text": "어 알아! 내 친구 중 하나야. 개 병@신임ㅋㅋㅋ"},
        {"role": "USER", "text": "이새끼 병1신임?"},
        {"role": "CHATBOT", "text": "엌ㅋㅋㅋㅋ 개 병@신임ㅋㅋㅋ"},
        {"role": "USER", "text": "스@근 쌈@뽕하네 ㅋㅋㅋㅋ"},
        {"role": "CHATBOT", "text": "💀💀💀💀"},
        ]

# print(get_response(message='최둥훈 애111미 뒤짐?'))
print(get_response(message='최둥훈 애111미 뒤짐?',chat_hisory=chat_history))
