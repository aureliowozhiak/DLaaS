import requests
from bs4 import BeautifulSoup

class WebPageDataScrappers:
    def __init__(self, url):
        self.url = url
        self.html_soup_content = BeautifulSoup(requests.get(self.url).content, 'html.parser')
    
    def getTagContent(self, tag_name):
        return self.html_soup_content.find_all(tag_name)
    
    def getHtml(self):
        return str(self.html_soup_content)

    def handleContent(self, tag_name, attrs):
        contents = []
        for tagContent in self.getTagContent(tag_name):
            tag_contents = []
            for attr in attrs:
                if tagContent.has_attr(attr):
                    tag_contents.append(tagContent[attr])
                if attr == "get_text":
                    tag_contents.append(tagContent.get_text())
            contents.append(tag_contents)

        return contents
        