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
            temperature       :float  = 0.3,
            max_tokens        :int    = 128, #TODO => can be flexible with Input Length!!
            frequency_penalty :float  = 1 # TODO => Main에 반영하기.. 둘다쓰네?
            ):
        
        response = co.chat(
                message           = message,
                chat_history      = chat_hisory,
                preamble          = preamble,
                model             = model,
                # temperature       = temperature,
                # max_tokens        = max_tokens,
                # frequency_penalty = frequency_penalty
        )
        print(chat_hisory)
        return response.text #TODO: 다른 정보도 쓰자
