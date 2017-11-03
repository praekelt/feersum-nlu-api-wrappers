# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.

    OpenAPI spec version: 2.0.2
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into model package
from .class_label import ClassLabel
from .class_label_list import ClassLabelList
from .class_label_pair import ClassLabelPair
from .create_details import CreateDetails
from .dashboard_detail import DashboardDetail
from .dashboard_model_detail import DashboardModelDetail
from .date import Date
from .date_list import DateList
from .duckling_ent_create_details import DucklingEntCreateDetails
from .duckling_instance_detail import DucklingInstanceDetail
from .duckling_instance_detail_list import DucklingInstanceDetailList
from .entity import Entity
from .entity_list import EntityList
from .instance_detail import InstanceDetail
from .instance_detail_list import InstanceDetailList
from .labeled_word_manifold import LabeledWordManifold
from .labelled_text_sample import LabelledTextSample
from .labelled_text_sample_list import LabelledTextSampleList
from .lr4_create_details import Lr4CreateDetails
from .lr4_instance_detail import Lr4InstanceDetail
from .lr4_instance_detail_list import Lr4InstanceDetailList
from .new_word import NewWord
from .new_word_list import NewWordList
from .regex_ent_create_details import RegexEntCreateDetails
from .regex_instance_detail import RegexInstanceDetail
from .regex_instance_detail_list import RegexInstanceDetailList
from .scored_label import ScoredLabel
from .scored_label_list import ScoredLabelList
from .sentiment import Sentiment
from .similarity_ent_create_details import SimilarityEntCreateDetails
from .similarity_instance_detail import SimilarityInstanceDetail
from .similarity_instance_detail_list import SimilarityInstanceDetailList
from .text_input import TextInput
from .total_samples import TotalSamples
from .train_details import TrainDetails
