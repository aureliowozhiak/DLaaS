import requests
from bs4 import BeautifulSoup

class WebPageDataScrappers:
    def __init__(self, url):
        self.url = url
        self.html_soup_content = BeautifulSoup(requests.get(self.url).content, 'html.parser')
    
    def getTagContent(self, tag_name):
       return [str(tag) for tag in self.html_soup_content.find_all(tag_name)]

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
        
    def countWords(self):
        text_content = self.html_soup_content.get_text()
        words = text_content.split()
        return len(words)

    def getImages(self):
        img_tags = self.html_soup_content.find_all('img')
        return [img.get('src') for img in img_tags if img.get('src')]

    def countTags(self, tag_name):
        tag_count = len(self.html_soup_content.find_all(tag_name))
        return tag_count

    def getMetaTags(self):
        meta_tags = self.html_soup_content.find_all('meta')
        meta_data = {}
        for meta in meta_tags:
            name = meta.get('name')
            content = meta.get('content')
            if name and content:
                meta_data[name] = content
        return meta_data

    def searchText(self, search_text):
        text_content = self.html_soup_content.get_text()
        occurrences = [line.strip() for line in text_content.splitlines() if search_text in line]
        return occurrences
