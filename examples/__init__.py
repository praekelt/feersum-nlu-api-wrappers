import os

# feersumnlu_host = "http://127.0.0.1:8080/nlu/v2"
feersumnlu_host = "http://127.0.0.1:8100/nlu/v2"
# feersumnlu_host = "https://nlu.playground.feersum.io:443/nlu/v2"


# Try to get the API key from your OS environment, else use 'YOUR_API_KEY' as the default value in the code below.
# You may use any environment variable you want, it doesn't have to be 'FEERSUM_NLU_AUTH_TOKEN'.
feersum_nlu_auth_token = os.environ.get('FEERSUM_NLU_AUTH_TOKEN', 'YOUR_API_KEY')
print('feersum_nlu_auth_token = ', feersum_nlu_auth_token)
