

from tokenizers import Tokenizer  
import requests

# download the tokenizer

tokenizer_url = " https://api.cohere.com/v1/models/command-r-plus" # use /models/<id> endpoint for latest URL

response = requests.get(tokenizer_url)  
tokenizer = Tokenizer.from_str(response.text)

tokenizer.encode(sequence="...", add_special_tokens=False)
