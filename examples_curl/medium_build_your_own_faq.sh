#!/bin/bash

SERVICE="http://127.0.0.1:8100"
# SERVICE="https://nlu.playground.feersum.io:443"

AUTH_TOKEN=$FEERSUM_NLU_AUTH_TOKEN  # "YOUR_API_KEY"
MODEL_NAME="medium_faq_mtchr"

A1="faq_tire"
A2="faq_engine"
A3="faq_accident"

A1Q1="How does one change a flat tire?"
A1Q2="What should I do if I have a puncture?"
A1Q3="Hoe ruil ek my kar se band?"
A1Q4="My wiel is pap. Wat nou?"

A2Q1="My car's engine won't start?"
A2Q2="I think my battery is dead?"
A2Q3="My kar wil nie vat nie?"
A2Q4="Ek dink my battery is pap?"

A3Q1="What should I do if I was in an accident?"
A3Q2="Please help I crashed my car."
A3Q3="Wat moet ek doen as ek in 'n ongeluk was?"
A3Q4="Help, ek het my kar gestamp"


#===
#create FAQ

curl -XPOST -is "$SERVICE"'/nlu/v2/faq_matchers' \
    -H "AUTH_TOKEN: $AUTH_TOKEN" \
    -H "accept: application/json" \
    -H "content-type: application/json" \
    -d '{"name":"'"$MODEL_NAME"'", "desc":"Test FAQ matcher.", "load_from_store": false}'


#===
# Submit training data.

curl -XPOST -is "$SERVICE"'/nlu/v2/faq_matchers/'"$MODEL_NAME"'/training_samples' \
    -H "AUTH_TOKEN: $AUTH_TOKEN" \
    -H "accept: application/json" \
    -H "content-type: application/json" \
    -d '['\
'{"text":"'"$A1Q1"'", "label":"'"$A1"'"},'\
'{"text":"'"$A1Q2"'", "label":"'"$A1"'"},'\
'{"text":"'"$A1Q3"'", "label":"'"$A1"'"},'\
'{"text":"'"$A1Q4"'", "label":"'"$A1"'"},'\
'{"text":"'"$A2Q1"'", "label":"'"$A2"'"},'\
'{"text":"'"$A2Q2"'", "label":"'"$A2"'"},'\
'{"text":"'"$A2Q3"'", "label":"'"$A2"'"},'\
'{"text":"'"$A2Q4"'", "label":"'"$A2"'"},'\
'{"text":"'"$A3Q1"'", "label":"'"$A3"'"},'\
'{"text":"'"$A3Q2"'", "label":"'"$A3"'"},'\
'{"text":"'"$A3Q3"'", "label":"'"$A3"'"},'\
'{"text":"'"$A3Q4"'", "label":"'"$A3"'"}'\
']'


#===
# Train
# - the 'threshold' parameter is useful to filter out weak matches. It is usually set to 0.85.
curl -XPOST -is "$SERVICE"'/nlu/v2/faq_matchers/'"$MODEL_NAME"'/train' \
    -H "AUTH_TOKEN: $AUTH_TOKEN" \
    -H "accept: application/json" \
    -H "content-type: application/json" \
    -d '{"immediate_mode": true, "threshold": 1.0, "word_manifold_list": [{"label": "eng", "word_manifold": "feers_wm_eng"}, {"label": "afr", "word_manifold": "feers_wm_afr"}]}'


#===
#Retrieve/test

# - Demonstrate a weak match of petrol to engine.
curl -XPOST -is "$SERVICE"'/nlu/v2/faq_matchers/'"$MODEL_NAME"'/retrieve' \
    -H "AUTH_TOKEN: $AUTH_TOKEN" \
    -H "accept: application/json" \
    -H "content-type: application/json" \
    -d '{"text": "I think I need petrol?"}'


# - Demonstrate a verb to noun match of verongeluk to ongeluk.
curl -XPOST -is "$SERVICE"'/nlu/v2/faq_matchers/'"$MODEL_NAME"'/retrieve' \
    -H "AUTH_TOKEN: $AUTH_TOKEN" \
    -H "accept: application/json" \
    -H "content-type: application/json" \
    -d '{"text": "Ek het my kar verongeluk?"}'
