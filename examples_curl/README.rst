Feersum NLU HTTP API Curl Examples
**********************************

The below commands can be run from a bash or similar terminal

.. code-block:: sh

    # === Setup some environment variables ===
    # SERVICE="http://127.0.0.1:8100"
    SERVICE="https://nlu.playground.feersum.io:443"

    AUTH_TOKEN="YOUR_API_KEY"
    
    # Note: One can get the below and more curl commands from 'trying out' commands from the 
    # swagger generated UI at <https://nlu.playground.feersum.io:443/nlu/v2/ui/>


.. code-block:: sh

    # === Get an overview of your loaded models by using the dashboard endpoint ===
    curl -XGET "$SERVICE"'/nlu/v2/dashboard' \
    	-H 'Content-Type: application/json' \
    	-H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN"


.. code-block:: sh

    # === Detect some sentiment ===
    curl -XPOST "$SERVICE"'/nlu/v2/sentiment_detectors/generic/retrieve' \
    	-H 'Content-Type: application/json' \
    	-H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
    	-d '{"text": "I am happy."}' 


.. code-block:: sh

    # === Parse a date ===
    curl -XPOST "$SERVICE"'/nlu/v2/date_parsers/generic/retrieve' \
    	-H 'Content-Type: application/json' \
    	-H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
    	-d '{"text": "The day after tomorrow at 11:00 in the morning."}' 


.. code-block:: sh

    # === Do text language identification ===
    # Create the model:
    curl -XPOST "$SERVICE"'/nlu/v2/lr4_language_recognisers' \
    	-H 'Content-Type: application/json' \
    	-H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
    	-d '{"desc": "LR4 text lang ID model.", "lid_model_file": "lid_za", "name": "test_model"}'

    # Detect the language of a piece of text:
    curl -XPOST "$SERVICE"'/nlu/v2/lr4_language_recognisers/test_model/retrieve' \
    	-H 'Content-Type: application/json' \
    	-H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
    	-d '{"text": "Watter taal praat ek?"}' 


.. code-block:: sh

    # === Do text classification ===
    # Create the model:
    curl -XPOST "$SERVICE"'/nlu/v2/text_classifiers' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '{"desc": "Example text classifier", "load_from_store": false, "name": "txt_clsfr_ex_1"}' 

    # Provide training data:
    curl -XPOST "$SERVICE"'/nlu/v2/text_classifiers/txt_clsfr_ex_1/training_samples' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '[{"label": "greeting", "text": "hello"}]' 

    curl -XPOST "$SERVICE"'/nlu/v2/text_classifiers/txt_clsfr_ex_1/training_samples' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '[{"label": "greeting", "text": "hi"}]' 

    curl -XPOST "$SERVICE"'/nlu/v2/text_classifiers/txt_clsfr_ex_1/training_samples' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '[{"label": "question", "text": "What is your name?"}]' 

    curl -XPOST "$SERVICE"'/nlu/v2/text_classifiers/txt_clsfr_ex_1/training_samples' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '[{"label": "question", "text": "How do I?"}]' 

    curl -XPOST "$SERVICE"'/nlu/v2/text_classifiers/txt_clsfr_ex_1/training_samples' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '[{"label": "question", "text": "When should one?"}]' 

    # Get the training data (for your info):
    curl -XGET "$SERVICE"'/nlu/v2/text_classifiers/txt_clsfr_ex_1/training_samples' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN"

    # Train the model:
    curl -XPOST "$SERVICE"'/nlu/v2/text_classifiers/txt_clsfr_ex_1/train' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '{"immediate_mode": true}' 

    # Make predictions using the model:
    curl -XPOST "$SERVICE"'/nlu/v2/text_classifiers/txt_clsfr_ex_1/retrieve' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '{"text": "hello"}' 


.. code-block:: sh

    # === Do natural language FAQ matching ===
    # See examples_curl/medium_build_your_own_faq.sh


.. code-block:: sh

    # === Do intent classification ===
    # See medium_build_your_own_faq.sh

    # Create the model:
    curl -XPOST "$SERVICE"'/nlu/v2/intent_classifiers' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '{"desc": "Example text classifier", "load_from_store": false, "name": "intent_clsfr_ex_1"}' 

    # Provide training data:
    curl -XPOST "$SERVICE"'/nlu/v2/intent_classifiers/intent_clsfr_ex_1/training_samples' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '[{"label": "greeting", "text": "hello"}]' 

    curl -XPOST "$SERVICE"'/nlu/v2/intent_classifiers/intent_clsfr_ex_1/training_samples' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '[{"label": "greeting", "text": "hi"}]' 

    curl -XPOST "$SERVICE"'/nlu/v2/intent_classifiers/intent_clsfr_ex_1/training_samples' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '[{"label": "question", "text": "What is your name?"}]' 

    curl -XPOST "$SERVICE"'/nlu/v2/intent_classifiers/intent_clsfr_ex_1/training_samples' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '[{"label": "question", "text": "How do I?"}]' 

    curl -XPOST "$SERVICE"'/nlu/v2/intent_classifiers/intent_clsfr_ex_1/training_samples' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '[{"label": "question", "text": "When should one?"}]' 

    # Get the training data (for your info):
    curl -XGET "$SERVICE"'/nlu/v2/intent_classifiers/intent_clsfr_ex_1/training_samples' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN"

    # Train the model:
    curl -XPOST "$SERVICE"'/nlu/v2/intent_classifiers/intent_clsfr_ex_1/train' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '{"immediate_mode": true}' 

    # Make predictions using the model:
    curl -XPOST "$SERVICE"'/nlu/v2/intent_classifiers/intent_clsfr_ex_1/retrieve' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
    	-H 'AUTH_TOKEN: '"$AUTH_TOKEN" \
        -d '{"text": "what is you name?"}' 
