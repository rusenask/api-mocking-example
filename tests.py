import unittest
import os
import requests
import json

from main import get_weather


HOVERFLY_ADMIN = os.environ.get("HOVERFLY_ADMIN", None)
HOVERFLY = os.environ.get("HOVERFLY", None)


class TestGetWeather(unittest.TestCase):

    def setUp(self):
        """
        Import data to Hoverfly
        """

        self.assertIsNotNone(HOVERFLY_ADMIN)
        with open('testing_resources/london_requests.json') as data_file:
            # importing captured requests for this test
            data = json.load(data_file)
            resp = requests.post(HOVERFLY_ADMIN + "records", json=data)
            self.assertEqual(resp.status_code, 200)
            # setting proxy environment variable
            os.environ["HTTP_PROXY"] = HOVERFLY

    def tearDown(self):
        """
        Delete test data from Hoverfly
        """
        # setting HTTP_PROXY variable to "" so it doesn't use proxy
        os.environ["HTTP_PROXY"] = ""
        # deleting records
        resp = requests.delete(HOVERFLY_ADMIN + "records")
        self.assertEqual(resp.status_code, 200)

    def test_get_london_weather(self):
        weather = get_weather("London")

        self.assertEqual(weather['body']['name'], 'London')
        self.assertEqual(weather['body']['main']['temp'], 284.69)
        self.assertEqual(weather['body']['main']['temp_max'], 286.48)
        self.assertEqual(weather['body']['main']['temp_min'], 283.15)

if __name__ == '__main__':
    unittest.main()
