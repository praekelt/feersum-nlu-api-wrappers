""" Example: Shows how to create & train an Intent classifier from a CSV file. """

import urllib3
import csv
import random

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'navigation2'
# instance_name = 'rewards_navigation'

create_details = feersum_nlu.IntentClassifierCreateDetails(name=instance_name,
                                                           lid_model_file="lid_za",
                                                           load_from_store=False)


def get_utterances(utterance_file: str):
    # with open(utterance_file, 'r') as txtfile:
    #     user_utterances = txtfile.readlines()

    user_utterances = []

    with open(utterance_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in csvreader:
            if len(row) > 0:
                utterance = row[0]
                user_utterances.append(utterance)

    random.shuffle(user_utterances)

    min_length = 5000
    req_length = max(len(user_utterances) // 100, min_length)

    return user_utterances[:req_length]


caller_name = 'example_caller'

print()
try:
    file_name_base = "dstv_exports"
    file_names = [
        "Add Movies.csv",
        "Change Package.csv",
        "Chat to Agent.csv",
        "Check Balance.csv",
        "Disney.csv",
        "Fix Error.csv",
        "Internet.csv",
        "Main Menu.csv",
        "Reconnect.csv",
        "Rewards.csv",
        "Third Party Payments.csv"
    ]

    for file_name in file_names:
        print(f"FILENAME = {file_name}")

        user_utterances = get_utterances(f"{file_name_base}/{file_name}")
        unmatched_count = 0

        output_file = f"{file_name_base}/{file_name}"

        with open(f"{output_file}_pred_labels.csv", "w", newline='') as csvfile:
            csv_writer = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['label', 'text'])

            for index, text in enumerate(user_utterances):
                text_input = feersum_nlu.TextInput(text.strip())
                api_response = api_instance.intent_classifier_retrieve(instance_name, text_input, x_caller=caller_name)
                # print("text_input", text_input)
                # print(" type(api_response)", type(api_response))
                # print(" api_response", api_response)
                if len(api_response) == 0:
                    unmatched_count += 1
                    pred_label = '_nc'
                else:
                    pred_label = api_response[0].label

                csv_writer.writerow([pred_label, text.strip()])
                if (index % 100) == 99:
                    print(f'    progress={round(10000.0 * index / len(user_utterances)) / 100.0}%: '
                          f'unmatched={round(10000.0 * unmatched_count / (index + 1)) / 100.0}%')

            print(f'    progress=100.0%: unmatched={round(10000.0 * unmatched_count / (index + 1)) / 100.0}%')

except ApiException as e:
    print("Exception when calling an Intent classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
