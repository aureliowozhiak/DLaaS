import requests
import json


class ApiRequests:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def make_request(self, endpoint, method="GET", params=None, data=None):
        url = f"{self.base_url}/{endpoint}"
        print(url)
        response = requests.request(
            method, url, headers=self.headers, params=params, data=data
        )
        return response
    
    #usign make_request method base create a pagination method passing the endpoint and a dict like this:
    #  "page":
    #           {
    #               "page_start": 1,
    #               "page_step":1,
    #               "page_end": 3
    #           }
    #   "page_start" is the first page to be requested
    #   "page_step" is the step between pages
    #   "page_end" is the last page to be requested
    #   "page_start" and "page_end" are inclusive
    def make_full_request(
        self, endpoint, method="GET", params=None, data=None, pagination=None
    ):
        if pagination is None:
            return self.make_request(endpoint, method, params, data)

        page_start = pagination["page_start"]
        page_step = pagination["page_step"]
        page_end = pagination["page_end"]

        responses = {}
        for page in range(page_start, page_end + 1, page_step):
            page_params = {"page": page}
            response = self.make_request(endpoint, method, page_params, data)
            responses[page] = response.json()
            
        return responses
    

