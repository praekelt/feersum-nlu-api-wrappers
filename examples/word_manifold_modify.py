# The word manifold endpoint have been removed while developing the new language model endpoints!

# """ Example: Shows how to create & modify (requires special permission) as well as use word manifolds. """
#
# import urllib3
#
# import feersum_nlu
# from feersum_nlu.rest import ApiException
# from examples import feersumnlu_host, feersum_nlu_auth_token
#
# # Configure API key authorization: APIKeyHeader
# configuration = feersum_nlu.Configuration()
#
# # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
# configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!
#
# configuration.host = feersumnlu_host
#
# api_instance = feersum_nlu.WordManifoldsApi(feersum_nlu.ApiClient(configuration))
#
# instance_name = 'feers_wm_eng'
# new_word_list = [{'new_word': 'chatbot', 'similar_to': 'robot'}]  # NewWordList | List of new words.
#
# new_word_list_b = [{'new_word': 'chatbots', 'similar_to': 'robots'},
#                    {'new_word': 'shaki', 'similar_to': 'brown'}]  # NewWordList | List of new words.
#
# create_details = feersum_nlu.WordManifoldCreateDetails(name=instance_name,
#                                                        desc="Test word manifold.",
#                                                        word_vectors_file="glove.6B.50d.trimmed.txt",
#                                                        load_from_store=False)  # file present on server
#
# # create_details = feersum_nlu.WmCreateDetails(name=instance_name, load_from_store=True)
#
# print()
#
# try:
#     # print("Create the word manifold model:")
#     # api_response = api_instance.word_manifold_create(create_details)
#     # print(" type(api_response)", type(api_response))
#     # print(" api_response", api_response)
#     # print()
#
#     print("Add some new words to the manifold and save the updated version:")
#     api_response = api_instance.word_manifold_add_similar_words(instance_name, new_word_list)
#     print(" type(api_response)", type(api_response))
#     print(" api_response", api_response)
#     print()
#
#     print("Add some new words to the manifold and save the updated version:")
#     api_response = api_instance.word_manifold_add_similar_words(instance_name, new_word_list_b)
#     print(" type(api_response)", type(api_response))
#     print(" api_response", api_response)
#     print()
#
# except ApiException as e:
#     print("Exception when calling a word manifold operation: %s\n" % e)
# except urllib3.exceptions.HTTPError as e:
#     print("Connection HTTPError! %s\n" % e)
