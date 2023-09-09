from unittest import TestCase
from unittest.mock import MagicMock

import requests

from .webPageDataScrappers import WebPageDataScrappers

test_html = ''.join(
    ['<html><head><meta content="text/html; charset=utf-8"',
     ' http-equiv="Content-Type" name="test-tag"/>',
     '<meta/></head>',
     '<p>paragraph 1</p><p>paragraph 2</p><img src="img-src-1"/>',
     '<img src="img-src-2"/></html>'])


class FakeResponse:
    def __init__(self, content):
        self.content = content


class WebPageDataScrappersTestSuite(TestCase):
    def setUp(self):
        requests.get = MagicMock(return_value=FakeResponse(test_html))

        self.url = "http://url.local"
        self.scrapper = WebPageDataScrappers(self.url)

    def test_can_get_html(self):
        html = self.scrapper.get_html()
        self.assertEqual(html, test_html)

    def test_can_get_tag_content(self):
        expected = ['<p>paragraph 1</p>', '<p>paragraph 2</p>']
        content = self.scrapper.get_tag_content("p")
        self.assertEqual([str(c) for c in content], expected)

    def test_can_handle_content_attr(self):
        expected = [['img-src-1'], ['img-src-2']]
        content = self.scrapper.handle_content(["img"], ["src"])
        self.assertEqual(content, expected)

    def test_can_handle_content_get_text(self):
        expected = [['paragraph 1'], ['paragraph 2']]
        content = self.scrapper.handle_content(["p"], ["get_text"])
        self.assertEqual(content, expected)

    def test_can_count_words(self):
        word_count = self.scrapper.count_words()
        self.assertEqual(word_count, 3)

    def test_can_get_images(self):
        expected = ['img-src-1', 'img-src-2']
        imgs = self.scrapper.get_images()
        self.assertEqual(imgs, expected)

    def test_can_count_tags(self):
        tag_count = self.scrapper.count_tags("p")
        self.assertEqual(tag_count, 2)

    def test_can_get_meta_tags(self):
        meta_tags = self.scrapper.get_meta_tags()
        self.assertEqual(meta_tags["test-tag"], "text/html; charset=utf-8")

    def test_can_search_text(self):
        expected = ['paragraph 1paragraph 2']
        result = self.scrapper.search_text("paragraph")
        self.assertEqual(result, expected)
