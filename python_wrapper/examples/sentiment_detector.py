import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
feersum_nlu.configuration.host = "http://127.0.0.1:8080/nlu/v2"

api_instance = feersum_nlu.SentimentDetectorsApi()

model_instance_name = 'generic'
text_input = feersum_nlu.TextInput("I am happy.") # TextInput | The input text.

try:
    # Detect sentiment.
    api_response = api_instance.sentiment_detector_retrieve(model_instance_name, text_input)
    print(api_response)
except ApiException as e:
    print("Exception when calling SentimentDetectorsApi->sentiment_detector_retrieve: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")

