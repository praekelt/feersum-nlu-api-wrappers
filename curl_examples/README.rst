Feersum NLU HTTP API Curl Examples
**********************************

The below commands can be run from a bash or similar terminal

.. code-block:: sh

    SERVICE="nlu.playground.feersum.io:8100"
    AUTH_TOKEN="YOUR_API_KEY"
    #
    # Note: One can get the below and more curl commands from 'trying out' commands from the 
    # swagger generated UI at <http://nlu.playground.feersum.io:8100/nlu/v2/ui/>


.. code-block:: sh

    # === Detect some sentiment ===
    curl -XPOST 'http://'"$SERVICE"'/nlu/v2/sentiment_detectors/generic/retrieve' \
    	-H 'Content-Type: application/json' \
    	-H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
    	-d '{"text": "I am happy."}' 


.. code-block:: sh

    # === Parse a date ===
    curl -XPOST 'http://'"$SERVICE"'/nlu/v2/date_parsers/generic/retrieve' \
    	-H 'Content-Type: application/json' \
    	-H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
    	-d '{"text": "The day after tomorrow at 11:00 in the morning."}' 


.. code-block:: sh

    # === Do text language identification ===
    # Create the model:
    curl -XPOST 'http://'"$SERVICE"'/nlu/v2/lr4_language_recognisers' \
    	-H 'Content-Type: application/json' \
    	-H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
    	-d '{"desc": "LR4 text lang ID model.", "model_file": "lid_za", "name": "test_model"}' 

    # Detect the language of a piece of text:
    curl -XPOST 'http://'"$SERVICE"'/nlu/v2/lr4_language_recognisers/test_model/retrieve' \
    	-H 'Content-Type: application/json' \
    	-H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
    	-d '{"text": "Watter taal praat ek?"}' 

