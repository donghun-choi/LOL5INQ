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
