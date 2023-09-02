from methods.extractors.webPageDataScrappers import WebPageDataScrappers
from methods.extractors.apiRequests import ApiRequests
from methods.extractors.databaseConnectors import MySQLConnector
from methods.loaders.fileSavers import FileSavers
import json
import os

config_path = 'config_files'

filesaver = FileSavers()

for filename in os.listdir(config_path):
    full_path = os.path.join(config_path, filename)
    if os.path.isfile(full_path):
        print(filename)
        with open(full_path, 'r') as file:
            config_file = json.load(file)

        

        for url,v in config_file.items():

            if "webscrapper" in filename:
                webscrapper = WebPageDataScrappers(url)
                for i in v:
                    filesaver.saveContent(webscrapper.handleContent(i["tag"], i["attrs"]), i["file_name"], i["attrs"], sep=i["sep"])
            
            if "api" in filename:
                for i in v:
                    response = json.dumps(ApiRequests(url, headers=i['api_headers']).make_request(i['endpoint_path']).json())

                    filesaver.saveContent(response, i["file_name"])

            if "mysql" in filename:
                host = url
                user = v["user"]
                password = v["password"]
                schema = v.get("schema") #opcional
                connector = MySQLConnector(
                    user=user, 
                    password=password,
                    host=host,
                    schema=schema
                )
                for table, output_file in v["tables"].items():
                    table_data = connector.extract(table)
                    filesaver.saveContent(table_data, output_file)