# The word manifold endpoint have been removed while developing the new language model endpoints!

# """ Example: Shows how to create and use word manifolds. """
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
# # The already loaded word embedding to use.
# instance_name = 'feers_wm_eng'
# # The playground's pre-loaded embeddings include:
# # "feers_wm_afr", "feers_wm_eng", "feers_wm_nbl", "feers_wm_xho",
# # "feers_wm_zul", "feers_wm_ssw", "feers_wm_nso", "feers_wm_sot",
# # "feers_wm_tsn", "feers_wm_ven", "feers_wm_tso"
# # and "glove6B50D_trimmed"
#
# word_and_threshold = feersum_nlu.WordAndThreshold('tree', 0.5)
# misspelt_word = feersum_nlu.TextInput('hospitle')
#
# try:
#     pass
#     # print("Find words similar to:")
#     # api_response = api_instance.word_manifold_get_similar_words(instance_name, word_and_threshold)
#     # print(" type(api_response)", type(api_response))
#     # print(" api_response", api_response)
#     # print()
#
#     # Spell check is not yet surfaced on the server.
#     # print("Spell correct:")
#     # api_response = api_instance.word_manifold_spell_correct(instance_name, misspelt_word)
#     # print(" type(api_response)", type(api_response))
#     # print(" api_response", api_response)
#     # print()
#
# except ApiException as e:
#     print("Exception when calling a word manifold operation: %s\n" % e)
# except urllib3.exceptions.HTTPError as e:
#     print("Connection HTTPError! %s\n" % e)
