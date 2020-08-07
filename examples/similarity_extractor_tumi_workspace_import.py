""" Example: Shows how similar word entity extractors may be created from a Watson workspace export. """

import urllib3
from typing import List, Dict
import json

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

entity_dict = {
    "entity": "Issues", "values": [
        {"type": "synonyms", "value": "Dashes", "synonyms": ["= = = =, 4 dashes , 4 lines", "= = = =", "4 lines"]},
        {"type": "synonyms", "value": "Times", "synonyms": ["The time"]},
        {"type": "synonyms", "value": "Red line", "synonyms": ["red exclamation mark", "red light", "orange light"]},
        {"type": "synonyms", "value": "Scan", "synonyms": ["2= = 2, 3 = = 3, Scan"]}, {"type": "synonyms", "value": "8118",
                                                                                       "synonyms": ["BE1", "STBY", "dddd",
                                                                                                    "Flashing = = =",
                                                                                                    "flashing 4 lines",
                                                                                                    "flashing 4 dashes",
                                                                                                    "bbbb",
                                                                                                    "flashing4 lines",
                                                                                                    "flashing dashes"]},
        {"type": "synonyms", "value": "Sound",
         "synonyms": ["distorted noise", "noise", "hear", "no volume", "mute", "terrible noise"]},
        {"type": "synonyms", "value": "pixelation",
         "synonyms": ["pixelation", "Pixilated", "distorted", "pixilation", "tiny blocks", "frozen", "breaking up",
                      "different shapes"]}, {"type": "synonyms", "value": "Blank screen",
                                             "synonyms": ["black", "black screen", "blue screen", "no light",
                                                          "Nothing, Black panel, Blank", "shows nothing", "blank"]},
        {"type": "synonyms", "value": "Channel Number", "synonyms": ["A channel number, A number", "number"]},
        {"type": "synonyms", "value": "TV", "synonyms": ["television", "tvs"]},
        {"type": "synonyms", "value": "Snowy", "synonyms": ["hazy", "fuzzy image", "snowy"]},
        {"type": "synonyms", "value": "working",
         "synonyms": ["working", "watch", "work", "faulty", "died", "problems", "not responding", "issues",
                      "Nothing happens",
                      "broken"]}]
}

entity_dict = {"entity": "Errors",
               "values": [{"type": "synonyms", "value": "E120", "synonyms": ["e 120", "e120-4", "e 120-4"]},
                          {"type": "synonyms", "value": "E109", "synonyms": ["e 109", "e109-4", "e 109-4"]},
                          {"type": "synonyms", "value": "E101", "synonyms": ["e 101", "e101-29", "e 101-29"]},
                          {"type": "synonyms", "value": "E017", "synonyms": ["e 017"]},
                          {"type": "synonyms", "value": "E-106", "synonyms": ["e106", "e 106", "e106 -4"]},
                          {"type": "synonyms", "value": "E48", "synonyms": ["e48", "E48-32", "E-48"]},
                          {"type": "synonyms", "value": "E44", "synonyms": ["e 44", "e44-32", "e 44-32"]},
                          {"type": "synonyms", "value": "signal", "synonyms": ["signal", "siganl"]},
                          {"type": "synonyms", "value": "LNK1020", "synonyms": ["1020", "lnk1020", "lnk 1020"]},
                          {"type": "synonyms", "value": "400", "synonyms": ["400"]},
                          {"type": "synonyms", "value": "Red", "synonyms": []},
                          {"type": "synonyms", "value": "Amber", "synonyms": ["amber light"]},
                          {"type": "synonyms", "value": "Green", "synonyms": ["green light"]},
                          {"type": "synonyms", "value": "E162", "synonyms": ["e 164", "e-162"]},
                          {"type": "synonyms", "value": "E76", "synonyms": ["e 76", "e76-32", "e 76-32"]},
                          {"type": "synonyms", "value": "E75", "synonyms": ["e 75", "e75-32", "e 75-32"]},
                          {"type": "synonyms", "value": "E73", "synonyms": ["e 73", "e73-32", "e 73-32"]},
                          {"type": "synonyms", "value": "E72", "synonyms": ["e 72", "e72-32", "e 72-32"]},
                          {"type": "synonyms", "value": "E71", "synonyms": ["e 71", "e71-32", "e 71-32"]},
                          {"type": "synonyms", "value": "E70", "synonyms": ["e 70", "e70-32", "e 70-32"]},
                          {"type": "synonyms", "value": "E600", "synonyms": ["e 600", "e600-4"]},
                          {"type": "synonyms", "value": "E45", "synonyms": ["e45-32", "e 45-32"]},
                          {"type": "synonyms", "value": "X", "synonyms": ["x", "error x", "x error", "cross"]},
                          {"type": "synonyms", "value": "E43", "synonyms": ["e 43", "e43-32", "e 43-32"]},
                          {"type": "synonyms", "value": "E42", "synonyms": ["e 42", "e42-32", "e 42-32"]},
                          {"type": "synonyms", "value": "E33", "synonyms": ["e 33", "e33-4", "e 33-4"]},
                          {"type": "synonyms", "value": "E31", "synonyms": ["e31", "e 31", "e31-0", "e 31-0"]},
                          {"type": "synonyms", "value": "E30", "synonyms": ["e30-4"]},
                          {"type": "synonyms", "value": "E144", "synonyms": ["e 144", "e144-4", "e 144-4"]},
                          {"type": "synonyms", "value": "E133", "synonyms": ["e 133", "e133-4", "e 133-4"]},
                          {"type": "synonyms", "value": "Title Issue",
                           "synonyms": ["catch up show", "catchup show", "catchup shows", "catch up shows", "no title",
                                        "title", "titles", "missing titles"]},
                          {"type": "synonyms", "value": "E107", "synonyms": ["e107", "e-107", "e107-4"]},
                          {"type": "synonyms", "value": "E102-29",
                           "synonyms": ["e102", "e-102", "subscription", "pvr functionality", "e 102"]},
                          {"type": "synonyms", "value": "E16", "synonyms": ["e-16", "e16-4", "e 16-4"]},
                          {"type": "synonyms", "value": "E18", "synonyms": ["e 18-4", "e18-4", "e 18", "e18", "E-18"]},
                          {"type": "synonyms", "value": "DStv Now app", "synonyms": ["DStv Now", "dstv.com"]},
                          {"type": "synonyms", "value": "Customer is not registered", "synonyms": []},
                          {"type": "synonyms", "value": "Error Codes", "synonyms": ["error", "errors"]},
                          {"type": "synonyms", "value": "CatchUp Plus Titles",
                           "synonyms": ["Catch Up Plus Titles", "CatchUp PlusTitles", "download", "streaming"]},
                          {"type": "synonyms", "value": "No Internet Connection",
                           "synonyms": ["is not coming", "isn't coming", "access to", "can't get", "internet connection",
                                        "internet connectivity", "No internet"]},
                          {"type": "synonyms", "value": "Incorrect Playout",
                           "synonyms": ["wrong episode", "wrong series", "wrong movie", "wrong title", "wrong sound",
                                        "wrong audio", "different", "something else", "not the one", "another", "incorrect",
                                        "wrong program", "right movie"]},
                          {"type": "synonyms", "value": "E50", "synonyms": ["e 50"]},
                          {"type": "synonyms", "value": "E143 Error",
                           "synonyms": ["waiting for communication", "E-143", "e143"]},
                          {"type": "synonyms", "value": "Playlist",
                           "synonyms": ["fast forward", "rewind", "pause", "PVR Functions", "record", "recording",
                                        "hard drive", "recorded", "hard disk", "disk"]},
                          {"type": "synonyms", "value": "E108", "synonyms": ["e108-4"]},
                          {"type": "synonyms", "value": "E100", "synonyms": ["e-100", "e 100", "e-100-4", "e100-4"]},
                          {"type": "synonyms", "value": "E37", "synonyms": ["e37", "e37-32"]},
                          {"type": "synonyms", "value": "E19-4", "synonyms": ["e19-4", "e19", "e 19-4", "E-19"]},
                          {"type": "synonyms", "value": "E38", "synonyms": []},
                          {"type": "synonyms", "value": "Content Not Updating", "synonyms": ["missing titles"]},
                          {"type": "synonyms", "value": "Picture", "synonyms": ["picture", "pic"]},
                          {"type": "synonyms", "value": "Sound", "synonyms": ["sound"]},
                          {"type": "synonyms", "value": "Customer does not meet criteria", "synonyms": []},
                          {"type": "synonyms", "value": "E32", "synonyms": ["e32", "E32-4"]},
                          {"type": "synonyms", "value": "E17", "synonyms": ["e17", "E17-4", "e-17"]},
                          {"type": "synonyms", "value": "E06", "synonyms": ["e06", "E05-4"]},
                          {"type": "synonyms", "value": "E05", "synonyms": ["e05", "E05-4"]},
                          {"type": "synonyms", "value": "E04", "synonyms": ["e04", "E04-4"]},
                          {"type": "synonyms", "value": "E118", "synonyms": ["e 118", "e118-4", "e 118-4"]}
                          ]
               }


def import_watson_workspace_extrs(filename: str) -> Dict[str, List[str]]:
    extr_words_dict = {}  # type: Dict[str, List[str]]

    with open(filename) as json_file:
        workspace = json.load(json_file)

        print(f"Workspace name = {workspace.get('name')}")

        entities = workspace.get('entities')
        # print(json.dumps(entities, indent=4))
        # print(len(entities))

        if entities is not None:
            for entity in entities:
                entity_name = entity.get('entity')
                entity_value_dicts = entity.get('values')

                if entity_name is not None and entity_value_dicts is not None:
                    for entity_value_dict in entity_value_dicts:
                        type = entity_value_dict.get('type')
                        value = entity_value_dict.get('value')

                        if type == 'synonyms' and value is not None:
                            synonyms = entity_value_dict.get('synonyms')

                            # print(entity_name, value, synonyms)
                            word_list = extr_words_dict.get(entity_name, [])
                            word_list.append(value)
                            word_list.extend(synonyms)

                            extr_words_dict[entity_name] = word_list

    return extr_words_dict


# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.SimWordEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

extr_words_dict = import_watson_workspace_extrs("data/watson-workspace-export-for-44a4bcc9-1fca-4580-aa6e-d683a2357e8a.json")

for extr_name, extr_words in extr_words_dict.items():

    extr_name = "tumi_" + extr_name + "_sw_extr"
    print(extr_name, extr_words)

    # exit(0)

    instance_name = extr_name

    similarity_ent_create_details = \
        feersum_nlu.SimWordEntityExtractorCreateDetails(name=instance_name,
                                                        desc=extr_name,
                                                        similar_words=extr_words,
                                                        threshold=0.75,
                                                        # (0.0-1.0] - lower vals result in more false positives.
                                                        word_manifold="feers_wm_eng",
                                                        # This is one of the built-in word embeddings.
                                                        load_from_store=False)

    text_input = feersum_nlu.TextInput("I have an orange car with pink stripes.")

    print()

    try:
        print("Create the entity extractor:")
        api_response = api_instance.sim_word_entity_extractor_create(similarity_ent_create_details)
        print(" type(api_response)", type(api_response))
        print(" api_response", api_response)
        print()

        print("Get the details of specific named loaded entity extractor:")
        api_response = api_instance.sim_word_entity_extractor_get_details(instance_name)
        print(" type(api_response)", type(api_response))
        print(" api_response", api_response)
        print()

        # print("Extract entities:")
        # api_response = api_instance.sim_word_entity_extractor_retrieve(instance_name, text_input)
        # print(" type(api_response)", type(api_response))
        # print(" api_response", api_response)
        # print()

        # print("Delete named loaded entity extractor:")
        # api_response = api_instance.sim_word_entity_extractor_del(instance_name)
        # print(" type(api_response)", type(api_response))
        # print(" api_response", api_response)
        # print()
        #
        # print("Vaporise named loaded entity extractor:")
        # api_response = api_instance.sim_word_entity_extractor_vaporise(instance_name)
        # print(" type(api_response)", type(api_response))
        # print(" api_response", api_response)
        # print()

    except ApiException as e:
        print("Exception when calling a entity extractor operation: %s\n" % e)
    except urllib3.exceptions.HTTPError as e:
        print("Connection HTTPError! %s\n" % e)
