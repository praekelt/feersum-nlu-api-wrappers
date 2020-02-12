Changelog
*********

Version 2.0.45
==============

Added the text and image labelled datasets endpoints to allow a user to create and manage labelled datasets.

Added a 'has_labels' flag to the model details returned on the dashboard. Useful to know which model types have a
'get_labels' endpoint.


Version 2.0.44
==============

Added the approximate (fuzzy) string matching text classifier.

Added the softmax temperature as a hyper parameter to the text, intent and FAQ classifiers.


Version 2.0.43
==============

Updated the sentiment model to add additional emoji sentiment mainly to support thumbs up/down.

Tested and fixed the emotion rest API.

Added the active log file's name to the dashboard response to know which file to download when needed.


Version 2.0.42
==============

Some example updates.

Changed the 'get_labels' rest api collection to a more resty 'labels'. No change to wrapper functions.


Version 2.0.41
==============

Added an SVM classifier algorithm option to the text classifier. The supported algorithms now are naive_bayes, svm, nearest_neighbour_l1,
and nearest_neighbour_cosine.

Added `collection_uri` to the dashboard's model detail. It is the URI of the model type's collection resource e.g. /faq_matchers
for the collection of faq_matcher models. Typically it is just the plural of the model type.

The model's uuid is now also returned in the dashboard model detail. The model history includes the current version of the model
only if the last update was pushed to the history.

The dashboard now also returns any custom sentence_encoders (language_models) and image_encoders (vision_models) that is loaded
for the API key.


Version 2.0.40
==============

Updated the 'update_samples' and 'update_samples'end points to just return a list of samples.


Version 2.0.39
==============

Added 'update_samples' response to update samples endpoints.

Added a samples put/update endpoint to update samples by uuid.


Version 2.0.38
==============

Updated the sample delete endpoints to allow one to delete samples by their UUIDs. The sample UUIDs are allocated by the
service and returned along with the samples from the get samples endpoints.


Version 2.0.37
==============

Updated the API key management interface to allow one to add an entry with an existing key.

The api key details response now includes an api call breakdown over the endpoints.


Version 2.0.36
==============

Added an emotion classifier model.

Added an image reader model for OCR and barcode reading applications.

Added optional index and len query params to the GET sample endpoints to allow one to split large sample
downloads over multiple calls in cases where the service config doesn't allow large responses.


Version 2.0.35
==============

Added num_epochs to the image classifier's train endpoint.

Added automatic class balancing added for the image classifier.

Updated the Python API wrapper for Python 3.7 using swagger-codegen 2.4.6.


Version 2.0.34
==============

Server patched, no functional updates.


Version 2.0.33
==============

Added image classifier endpoint.

Added LR4_language_recogniser alias for language_recogniser for compatibility with some older applications.

The dashboard now reports language models as sentence_encoders instead of word_manifolds. The sentence encoder model
also now returns the encoder type and language.

Added examples of how to use the text classifier using Naive Bayes and nearest neighbour L1 search (with different language
models).

The word manifold endpoint have been removed from the service while developing the new language model endpoints!

Add ignore word boundaries and ignore case flags to synonym extractor entities.


Version 2.0.31
==============

Added git-like revision control. One can now load a specific revision of a model by providing its UUID in the create endpoints.
The dashboard endpoint also now returns a model's revision history.

Added a second POST dashboard end-point that allows one to set some operation parameters like a model's history size to show.

Added a synonym entity extractor.

Added a convenience 'delete_all' endpoint for data objects.

Added a PrometheusHandler logging handler that logs counts of various log level emits to Prometheus.

Added X-Caller header param. E.g. x_caller='example_caller' in api call.




Version 2.0.29
==============

Added TSNE analytics to the intent model and its API. See 'examples/intent_classifier.py'.

Added model readonly flag which prevents a model from being modified or a new model of the same name being created.

Added CRF entity extractor.


Version 2.0.28
==============

Specialised the entity extractor response models from entity_model to duckling_entity, person_name_entity, regex_entity and sim_word_entity.


Version 2.0.27
==============

Added more samples to intent classifier to demonstrate cross validation.


Version 2.0.26
==============

Added import and export of models to a feersum_nlu_util.transfer module.


Version 2.0.25
==============

Added the threshold param (that used to be only on intents and FAQs) to the text classifier model.

Add num_training_samples and num_testing_samples to model instance details.

example/intent_classifier.py added example of providing a language hint.


Version 2.0.24
==============

Added mypy, pylint, flake8, coverage and coveralls to dependencies.

example/intent_classifier.py updated to show how to get the model's editable parameters (intent_classifier_get_params).

example/dashboard.py updated to show how to retrieve response headers X-RateLimit-Remaining.



Version 2.0.23
==============

Added multi-part sentiment:

- The sentiment end-point use to return object {"value": 0.54}.

- Now it returns object {"detail_list": [{"index": 0,"len": 20,"value": 0.54}],"value": 0.54}.

- See class 'feersum_nlu.models.sentiment.Sentiment'

Added the vaporise endpoint to permanently delete a model instance whether it is trashed or not.

Added a lang_code hint to the retrieve/inference and data endpoints.


Version 2.0.22
==============

Name changes to make the Python API more consistent and friendlier towards code generation:

- text_clsfr_create_details renamed to text_classifier_create_details

- text_clsfr_instance_detail renamed to text_classifier_instance_detail

- wm_create_details renamed to word_manifold_create_details

- wm_instance_detail renamed to word_manifold_instance_detail

- create_details renamed to intent_classifier_create_details for intent classifier

- instance_detail renamed to intent_classifier_instance_detail for intent classifier

- create_details renamed to faq_matcher_create_details for faq matcher

- instance_detail renamed to faq_matcher_instance_detail for faq matcher

- regex_ent_create_details renamed to regex_entity_extractor_create_details

- regex_instance_detail renamed to regex_entity_extractor_instance_detail

- person_name_ent_create_details renamed to person_name_entity_extractor_create_details

- person_name_instance_detail renamed to person_name_entity_extractor_instance_detail

- duckling_ent_create_details renamed to duckling_entity_extractor_create_details

- duckling_instance_detail renamed to duckling_entity_extractor_instance_detail

- sim_word_ent_create_details renamed to sim_word_entity_extractor_create_details

- sim_word_instance_detail renamed to sim_word_entity_extractor_instance_detail

- lr4_language_recogniser renamed to language_recogniser

- lr4_create_details renamed to language_recogniser_create_details

- lr4_instance_detail renamed to language_recogniser_instance_detail


Version 2.0.21
==============

- Examples of async training.

- Examples of online training.


Version 2.0.20
==============

- Changed name of similar_entity_extractor to sim_word_entity_extractor.

- Removed the api hit counts from the dashboard.

- Added a trashed flag to each model in the dashboard.

- Removed the immediate_mode arguments in the train operations.

- The spec and Python API wrapper have been updated to rather return lists of python objects as opposed to lists of json objects.

- Changes to LR4 to have a load from store that works like all of the other names.


Version 2.0.18
==============

- Added a 'long_name' attribute to all models. May be used as a 'pretty' formatted model name while the existing model name is really a slug used in urls, etc.

- Addition of params end point to all models.  Used to update and get model attributes like desc, long_name and threshold.

- Updated LID LR4 to load from store.


Version 2.0.16
==============

- Added model delete endpoints.

- Expose experimental person name entity extractor on the http API.

- Exposed the reference_time attribute to the Duckling entity extractor.

- Moved the examples' and tests' auth token and host config to a central location in the __init.py__

- Added this changelog.



