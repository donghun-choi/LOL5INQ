import cohere
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

co = cohere.Client(os.getenv('COHERE_TOKEN'))

def get_response(
            message             :str,
    #       chat_hisory         :???    = None,
            preamble            :str    = None,
            model               :str    = 'command-r-plus',
            temperature         :float  = 1,
            max_tokens          :int    = 128,
            frequency_penalty   :float  = 1.0
            ):

    response = co.chat(
            message             = message,
    #       chat_history        = chat_hisory,
            preamble            = preamble,
            model               = model,
            temperature         = temperature,
            max_tokens          = max_tokens,
            frequency_penalty    = frequency_penalty
    )
    return response.text

# 가자 ㅇ예쁜 코드.
#TODO : Class화 시켜서 Main에서 쓸까?