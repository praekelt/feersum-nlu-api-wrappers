# coding: utf-8

from __future__ import absolute_import

import urllib3
import unittest
import time

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token

import uuid


class TestDucklingExtractorPerf(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_duckling_extractor(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.DucklingEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

        instance_name = 'test_duckling_extr_' + str(uuid.uuid4())

        duckling_ent_create_details = \
            feersum_nlu.DucklingEntityExtractorCreateDetails(name=instance_name,
                                                             desc="Test duckling extractor.",
                                                             load_from_store=False)

        text_input = feersum_nlu.TextInput("5 January 2017 at 15:00.")

        print()

        try:
            print("Create the entity extractor:")
            api_response = api_instance.duckling_entity_extractor_create(duckling_ent_create_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of all loaded entity extractors:")
            api_response = api_instance.duckling_entity_extractor_get_details_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded entity extractor:")
            api_response = api_instance.duckling_entity_extractor_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Extract entities:")
            api_response = api_instance.duckling_entity_extractor_retrieve(instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            entity_list = api_response
            if len(entity_list) > 0:
                entity = entity_list[0]
                self.assertTrue((entity.value == '2017-01-05T15:00:00.000+02:00') or
                                (entity.value == '2017-01-05T15:00:00.000Z'))
            else:
                self.assertTrue(False)

            print("Doing performance tests ...")
            num_iterations = 100
            start_time = time.time()
            for i in range(num_iterations):
                api_response = api_instance.duckling_entity_extractor_retrieve(instance_name, text_input)

                if ((i % 10) == 0) or (i == (num_iterations-1)):
                    print(f"{round(i*100.0/(num_iterations-1), 0)}%...", end="", flush=True)

                scored_label_list = api_response
                if len(scored_label_list) > 0:
                    scored_label = scored_label_list[0]
                    self.assertTrue((entity.value == '2017-01-05T15:00:00.000+02:00') or
                                    (entity.value == '2017-01-05T15:00:00.000Z'))
                else:
                    self.assertTrue(False)

            end_time = time.time()
            request_time = (end_time-start_time) / num_iterations
            print("done.")
            print(f"Time per request = {round(request_time, 3)}s.")
            print()

            print("Delete named loaded entity extractor:")
            api_response = api_instance.duckling_entity_extractor_del(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Vaporise named loaded entity extractor:")
            api_response = api_instance.duckling_entity_extractor_vaporise(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            self.assertTrue(request_time < 0.4)

        except ApiException as e:
            print("Exception when calling a entity extractor operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
