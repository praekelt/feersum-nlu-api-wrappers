# coding: utf-8

# flake8: noqa
"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.28
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from feersum_nlu.models.class_label import ClassLabel
from feersum_nlu.models.class_label_pair import ClassLabelPair
from feersum_nlu.models.dashboard_detail import DashboardDetail
from feersum_nlu.models.dashboard_model_detail import DashboardModelDetail
from feersum_nlu.models.data_object import DataObject
from feersum_nlu.models.data_object_name import DataObjectName
from feersum_nlu.models.date_entity import DateEntity
from feersum_nlu.models.duckling_entity import DucklingEntity
from feersum_nlu.models.duckling_entity_extractor_create_details import DucklingEntityExtractorCreateDetails
from feersum_nlu.models.duckling_entity_extractor_instance_detail import DucklingEntityExtractorInstanceDetail
from feersum_nlu.models.faq_matcher_create_details import FaqMatcherCreateDetails
from feersum_nlu.models.faq_matcher_instance_detail import FaqMatcherInstanceDetail
from feersum_nlu.models.intent_classifier_create_details import IntentClassifierCreateDetails
from feersum_nlu.models.intent_classifier_instance_detail import IntentClassifierInstanceDetail
from feersum_nlu.models.labeled_word_manifold import LabeledWordManifold
from feersum_nlu.models.labelled_text_sample import LabelledTextSample
from feersum_nlu.models.language_recogniser_create_details import LanguageRecogniserCreateDetails
from feersum_nlu.models.language_recogniser_instance_detail import LanguageRecogniserInstanceDetail
from feersum_nlu.models.model_params import ModelParams
from feersum_nlu.models.new_word import NewWord
from feersum_nlu.models.person_name_entity import PersonNameEntity
from feersum_nlu.models.person_name_entity_extractor_create_details import PersonNameEntityExtractorCreateDetails
from feersum_nlu.models.person_name_entity_extractor_instance_detail import PersonNameEntityExtractorInstanceDetail
from feersum_nlu.models.regex_entity import RegexEntity
from feersum_nlu.models.regex_entity_extractor_create_details import RegexEntityExtractorCreateDetails
from feersum_nlu.models.regex_entity_extractor_instance_detail import RegexEntityExtractorInstanceDetail
from feersum_nlu.models.scored_label import ScoredLabel
from feersum_nlu.models.sentiment import Sentiment
from feersum_nlu.models.sentiment_detail import SentimentDetail
from feersum_nlu.models.sim_word_entity import SimWordEntity
from feersum_nlu.models.sim_word_entity_extractor_create_details import SimWordEntityExtractorCreateDetails
from feersum_nlu.models.sim_word_entity_extractor_instance_detail import SimWordEntityExtractorInstanceDetail
from feersum_nlu.models.text_classifier_create_details import TextClassifierCreateDetails
from feersum_nlu.models.text_classifier_instance_detail import TextClassifierInstanceDetail
from feersum_nlu.models.text_input import TextInput
from feersum_nlu.models.total_samples import TotalSamples
from feersum_nlu.models.train_details import TrainDetails
from feersum_nlu.models.word_and_distance import WordAndDistance
from feersum_nlu.models.word_and_threshold import WordAndThreshold
from feersum_nlu.models.word_manifold_create_details import WordManifoldCreateDetails
from feersum_nlu.models.word_manifold_instance_detail import WordManifoldInstanceDetail
