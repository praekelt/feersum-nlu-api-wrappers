# coding: utf-8

# flake8: noqa
"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.55
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from feersum_nlu.models.active_learner_candidates import ActiveLearnerCandidates
from feersum_nlu.models.active_learner_instance_detail import ActiveLearnerInstanceDetail
from feersum_nlu.models.api_key_create_details import ApiKeyCreateDetails
from feersum_nlu.models.api_key_instance_detail import ApiKeyInstanceDetail
from feersum_nlu.models.class_label import ClassLabel
from feersum_nlu.models.class_label_pair import ClassLabelPair
from feersum_nlu.models.crf_entity import CrfEntity
from feersum_nlu.models.crf_entity_extractor_create_details import CrfEntityExtractorCreateDetails
from feersum_nlu.models.crf_entity_extractor_instance_detail import CrfEntityExtractorInstanceDetail
from feersum_nlu.models.crf_sample import CrfSample
from feersum_nlu.models.dashboard_detail import DashboardDetail
from feersum_nlu.models.dashboard_model_detail import DashboardModelDetail
from feersum_nlu.models.dashboard_params import DashboardParams
from feersum_nlu.models.data_object import DataObject
from feersum_nlu.models.data_object_name import DataObjectName
from feersum_nlu.models.date_entity import DateEntity
from feersum_nlu.models.dual_entity_intent import DualEntityIntent
from feersum_nlu.models.dual_entity_intent_create_details import DualEntityIntentCreateDetails
from feersum_nlu.models.dual_entity_intent_instance_detail import DualEntityIntentInstanceDetail
from feersum_nlu.models.duckling_entity import DucklingEntity
from feersum_nlu.models.duckling_entity_extractor_create_details import DucklingEntityExtractorCreateDetails
from feersum_nlu.models.duckling_entity_extractor_instance_detail import DucklingEntityExtractorInstanceDetail
from feersum_nlu.models.entity_intent_sample import EntityIntentSample
from feersum_nlu.models.faq_matcher_create_details import FaqMatcherCreateDetails
from feersum_nlu.models.faq_matcher_instance_detail import FaqMatcherInstanceDetail
from feersum_nlu.models.image_classifier_create_details import ImageClassifierCreateDetails
from feersum_nlu.models.image_classifier_instance_detail import ImageClassifierInstanceDetail
from feersum_nlu.models.image_dataset_create_details import ImageDatasetCreateDetails
from feersum_nlu.models.image_dataset_instance_detail import ImageDatasetInstanceDetail
from feersum_nlu.models.image_detection import ImageDetection
from feersum_nlu.models.image_detector_create_details import ImageDetectorCreateDetails
from feersum_nlu.models.image_detector_instance_detail import ImageDetectorInstanceDetail
from feersum_nlu.models.image_input import ImageInput
from feersum_nlu.models.image_output import ImageOutput
from feersum_nlu.models.intent_classifier_create_details import IntentClassifierCreateDetails
from feersum_nlu.models.intent_classifier_instance_detail import IntentClassifierInstanceDetail
from feersum_nlu.models.labelled_image_detections import LabelledImageDetections
from feersum_nlu.models.labelled_image_sample import LabelledImageSample
from feersum_nlu.models.labelled_language_model import LabelledLanguageModel
from feersum_nlu.models.labelled_text_sample import LabelledTextSample
from feersum_nlu.models.labelled_word_manifold import LabelledWordManifold
from feersum_nlu.models.language_recogniser_create_details import LanguageRecogniserCreateDetails
from feersum_nlu.models.language_recogniser_instance_detail import LanguageRecogniserInstanceDetail
from feersum_nlu.models.model_params import ModelParams
from feersum_nlu.models.model_revision import ModelRevision
from feersum_nlu.models.new_word import NewWord
from feersum_nlu.models.paragraph import Paragraph
from feersum_nlu.models.person_name_entity import PersonNameEntity
from feersum_nlu.models.person_name_entity_extractor_create_details import PersonNameEntityExtractorCreateDetails
from feersum_nlu.models.person_name_entity_extractor_instance_detail import PersonNameEntityExtractorInstanceDetail
from feersum_nlu.models.regex_entity import RegexEntity
from feersum_nlu.models.regex_entity_extractor_create_details import RegexEntityExtractorCreateDetails
from feersum_nlu.models.regex_entity_extractor_instance_detail import RegexEntityExtractorInstanceDetail
from feersum_nlu.models.scored_image_detection import ScoredImageDetection
from feersum_nlu.models.scored_image_detections import ScoredImageDetections
from feersum_nlu.models.scored_label import ScoredLabel
from feersum_nlu.models.sentiment import Sentiment
from feersum_nlu.models.sentiment_detail import SentimentDetail
from feersum_nlu.models.seq2seq_resp import Seq2seqResp
from feersum_nlu.models.service_params import ServiceParams
from feersum_nlu.models.synonym_entity import SynonymEntity
from feersum_nlu.models.synonym_entity_extractor_create_details import SynonymEntityExtractorCreateDetails
from feersum_nlu.models.synonym_entity_extractor_instance_detail import SynonymEntityExtractorInstanceDetail
from feersum_nlu.models.synonym_sample import SynonymSample
from feersum_nlu.models.test_details import TestDetails
from feersum_nlu.models.text_classifier_create_details import TextClassifierCreateDetails
from feersum_nlu.models.text_classifier_get_labels import TextClassifierGetLabels
from feersum_nlu.models.text_classifier_instance_detail import TextClassifierInstanceDetail
from feersum_nlu.models.text_dataset_create_details import TextDatasetCreateDetails
from feersum_nlu.models.text_dataset_instance_detail import TextDatasetInstanceDetail
from feersum_nlu.models.text_input import TextInput
from feersum_nlu.models.train_details import TrainDetails
from feersum_nlu.models.tsne_sample import TsneSample
from feersum_nlu.models.tsne_settings import TsneSettings
from feersum_nlu.models.word_and_distance import WordAndDistance
from feersum_nlu.models.word_and_threshold import WordAndThreshold
from feersum_nlu.models.word_manifold_create_details import WordManifoldCreateDetails
from feersum_nlu.models.word_manifold_instance_detail import WordManifoldInstanceDetail
