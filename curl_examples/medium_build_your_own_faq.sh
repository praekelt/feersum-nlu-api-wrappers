#!/bin/bash

SERVICE="nlu.playground.feersum.io:443"

AUTH_TOKEN="YOUR_API_KEY"
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

curl -XPOST -is 'https://'"$SERVICE"'/nlu/v2/faq_matchers' \
    -H "AUTH_TOKEN: $AUTH_TOKEN" \
    -H "accept: application/json" -H "content-type: application/json" \
    -d '{"name":"'"$MODEL_NAME"'", "desc":"Test FAQ matcher.", "load_from_store": false}'


#===
# Submit training data.

curl -XPOST -is 'https://'"$SERVICE"'/nlu/v2/faq_matchers/'"$MODEL_NAME"'/training_samples' \
    -H "AUTH_TOKEN: $AUTH_TOKEN" \
    -H "accept: application/json" -H "content-type: application/json" \
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

curl -XPOST -is 'https://'"$SERVICE"'/nlu/v2/faq_matchers/'"$MODEL_NAME"'/train' \
    -H "AUTH_TOKEN: $AUTH_TOKEN" \
    -H "accept: application/json" -H "content-type: application/json" \
    -d '{"immediate_mode": true, "thresh_hold": 0.85, "word_manifold_list": {"eng": "feers_wm_eng", "afr": "feers_wm_afr"}}'


#===
#Retrieve/test

curl -XPOST -is 'https://'"$SERVICE"'/nlu/v2/faq_matchers/'"$MODEL_NAME"'/retrieve' \
    -H "AUTH_TOKEN: $AUTH_TOKEN" \
    -H "accept: application/json" -H "content-type: application/json" \
    -d '{"text": "I think I need petrol?"}'


curl -XPOST -is 'https://'"$SERVICE"'/nlu/v2/faq_matchers/'"$MODEL_NAME"'/retrieve' \
    -H "AUTH_TOKEN: $AUTH_TOKEN" \
    -H "accept: application/json" -H "content-type: application/json" \
    -d '{"text": "Ek het my kar verongeluk?"}'
