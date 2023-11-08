import requests


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
