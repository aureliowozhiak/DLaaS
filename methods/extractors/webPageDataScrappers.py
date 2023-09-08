import requests
from bs4 import BeautifulSoup


class WebPageDataScrappers:
    def __init__(self, url):
        self.url = url
        self.html_soup_content = BeautifulSoup(
            requests.get(self.url).content, "html.parser"
        )

    def get_tag_content(self, tag_name):
        return self.html_soup_content.find_all(tag_name)

    def get_html(self):
        return str(self.html_soup_content)

    def handle_content(self, tag_name, attrs):
        contents = []
        for tagContent in self.get_tag_content(tag_name):
            tag_contents = []
            for attr in attrs:
                if tagContent.has_attr(attr):
                    tag_contents.append(tagContent[attr])
                if attr == "get_text":
                    tag_contents.append(tagContent.get_text())
            contents.append(tag_contents)

        return contents

    def count_words(self):
        text_content = self.html_soup_content.get_text()
        words = text_content.split()
        return len(words)

    def get_images(self):
        img_tags = self.html_soup_content.find_all("img")
        return [img.get("src") for img in img_tags if img.get("src")]

    def count_tags(self, tag_name):
        tag_count = len(self.html_soup_content.find_all(tag_name))
        return tag_count

    def get_meta_tags(self):
        meta_tags = self.html_soup_content.find_all("meta")
        meta_data = {}
        for meta in meta_tags:
            name = meta.get("name")
            content = meta.get("content")
            if name and content:
                meta_data[name] = content
        return meta_data

    def search_text(self, search_text):
        text_content = self.html_soup_content.get_text()
        occurrences = [
            line.strip() for line in text_content.splitlines()
            if search_text in line
        ]
        return occurrences
