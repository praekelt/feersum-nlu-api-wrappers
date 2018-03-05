Changelog
*********

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
- Added a 'long_name' attribute to all models. May be used as a 'pretty' formatted model name while the previous model
  name is really a slug used in urls, etc.

- Addition of params end point to all models.  Used to update and get model attributes like desc, long_name and threshold.

- Updated LID LR4 to load from store.


Version 2.0.16
==============

- Added model delete endpoints.

- Expose experimental person name entity extractor on the http API.

- Exposed the reference_time attribute to the Duckling entity extractor.

- Moved the examples' and tests' auth token and host config to a central location in the __init.py__

- Added this changelog.



