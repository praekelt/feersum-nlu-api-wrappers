Changelog
*********

Version 2.0.30
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



