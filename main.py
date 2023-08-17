from methods.extractors.webPageDataScrappers import WebPageDataScrappers
from methods.loaders.fileSavers import FileSavers
import json


#attrs = ["href","get_text"]
#filesaver.saveContent(webscrapper.handleContent("a", attrs), "links.csv", attrs)
#filesaver.saveContent(webscrapper.getHtml(), "wiki_python.html")


#filesaver.saveContent(webscrapper.handleContent("a", attrs), "links.csv", attrs)

with open('config_file.json', 'r') as file:
    config_file = json.load(file)

filesaver = FileSavers()

for url,v in config_file.items():
    webscrapper = WebPageDataScrappers(url)
    for i in v:
        eval(f'filesaver.saveContent(webscrapper.handleContent("{i["tag"]}", {i["attrs"]}), "{i["file_name"]}", {i["attrs"]}, sep="{i["sep"]}")')