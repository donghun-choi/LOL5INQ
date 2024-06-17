import cohere
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

co = cohere.Client(os.getenv('COHERE_TOKEN'))

def response(
            message,
        #     chat_hisory         = None,
            preamble            = None,
            model               = 'command-r-plus',
            temperature         = 1,
            max_tokens          = 128,
            frequency_penalty   = 1
            ):

    response = co.chat(
            message             = message,
        #     chat_history        = chat_hisory,
            preamble            = preamble,
            model               = model,
            temperature         = temperature,
            max_tokens          = max_tokens,
            frequency_penalty    = frequency_penalty
    )
        
    return response.text