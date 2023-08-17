from methods.extractors.webPageDataScrappers import WebPageDataScrappers
from methods.loaders.fileSavers import FileSavers


webscrapper = WebPageDataScrappers("https://pt.wikipedia.org/wiki/Python")
filesaver = FileSavers()
attrs = ["href","get_text"]
filesaver.saveContent(webscrapper.handleContent("a", attrs), "links.csv", attrs)