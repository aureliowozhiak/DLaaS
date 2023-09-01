import requests

class ApiRequests:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers
    
    def makeRequest(self, endpoint, method='GET', params=None, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, params=params, data=data)
        return response