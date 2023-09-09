from unittest import TestCase
from unittest.mock import MagicMock

import requests

from .apiRequests import ApiRequests


class ApiRequestsTestSuite(TestCase):
    def setUp(self):
        self.base_url = "http://baseurl.local"
        self.apiRequests = ApiRequests(self.base_url)

    def test_can_make_requests(self):
        endpoint = "fake-endpoint"
        return_value = {"data": "data"}
        requests.request = MagicMock(return_value=return_value)

        response = self.apiRequests.make_request(endpoint)

        self.assertEqual(response, return_value)
        requests.request.assert_called_with(
            "GET",
            f"{self.base_url}/{endpoint}",
            headers=None,
            params=None,
            data=None,
        )
