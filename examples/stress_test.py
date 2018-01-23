import time
import requests
import json
import concurrent.futures

from examples import feersum_nlu_auth_token

host = "http://127.0.0.1:8100"
# host = "https://nlu.playground.feersum.io:443"


# Execute some rest commands
def test_rest(service, timeout):
    # Dashboard:
    # response = requests.get(str(service) + str('/nlu/v2/dashboard'),
    #                         headers={'Content-Type': 'application/json',
    #                                  'Accept': 'application/json',
    #                                  'X-Auth-Token': feersum_nlu_auth_token},
    #                         data={})

    # retrieve from test_faq_mtchr:
    response = requests.post(str(service) + str('/nlu/v2/faq_matchers/test_faq_mtchr/retrieve'),
                             headers={'Content-Type': 'application/json',
                                      'Accept': 'application/json',
                                      'X-Auth-Token': feersum_nlu_auth_token},
                             json={'text': "How can one get a quote?"},
                             timeout=timeout)

    response_status = response.status_code
    response_json = response.json()

    # response_json_str = json.dumps(response_json, indent=2) + "\n"
    response_json_str = json.dumps(response_json)

    return response_json_str == '[{"label": "quote", "probability": 0.3151551139568258}]'
    # return response_json_str
    # return response_status


num_requests = 10

start_time = time.time()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    future_to_response_dict = {}

    for id in range(num_requests):
        future_to_response_dict[executor.submit(test_rest,
                                                host,
                                                100.0)] = id

    for future in concurrent.futures.as_completed(future_to_response_dict):
        id = future_to_response_dict[future]

        try:
            response = str(future.result())
        except Exception as exc:
            print('ID %d generated: %s' % (id, exc))
        else:
            print('ID %d generated: %s' % (id, response))

end_time = time.time()

print('Requests per second =', num_requests / (end_time - start_time))
