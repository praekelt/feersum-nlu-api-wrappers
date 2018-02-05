Changelog
*********

Version 2.0.18
==============
- Added a 'long_name' attribute to all models. May be used as a 'pretty' formatted model name while the model name is really a slug.

- Addition of params end point to all models.  Used to update and get model attributes like desc, long_name and threshold.

- Updated LID LR4 to load from store.


Version 2.0.16
==============

- Added model delete endpoints.

- Expose experimental person name entity extractor on the http API.

- Exposed the reference_time attribute to the Duckling entity extractor.

- Moved the examples' and tests' auth token and host config to a central location in the __init.py__

- Added this changelog.



