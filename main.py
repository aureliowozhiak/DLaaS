import json
import os

from methods.extractors.apiRequests import ApiRequests
from methods.extractors.databaseConnectors import MySQLConnector
from methods.extractors.webPageDataScrappers import WebPageDataScrappers
from methods.loaders.fileSavers import FileSavers

config_path = "config_files"

filesaver = FileSavers()

for filename in os.listdir(config_path):
    full_path = os.path.join(config_path, filename)
    if os.path.isfile(full_path):
        print(filename)
        with open(full_path, "r") as file:
            config_file = json.load(file)

        for url, v in config_file.items():
            if "webscrapper" in filename:
                webscrapper = WebPageDataScrappers(url)
                for i in v:
                    filesaver.save_content(
                        webscrapper.handle_content(i["tag"], i["attrs"]),
                        i["file_name"],
                        i["attrs"],
                        sep=i["sep"],
                    )

            if "api" in filename:
                for i in v:
                    response = json.dumps(
                        ApiRequests(url, headers=i["api_headers"])
                        .make_request(i["endpoint_path"])
                        .json()
                    )
                    filesaver.save_content(response, i["file_name"])

            if "mysql" in filename:
                host = url
                user = v["user"]
                password = v["password"]
                schema = v.get("schema")  # opcional
                connector = MySQLConnector(
                    user=user, password=password, host=host, schema=schema
                )
                for table, table_config in v["tables"].items():
                    table_data = connector.extract(
                        table,
                        table_config.get("columns"),
                        table_config.get("where"),
                        table_config.get("limit"),
                    )
                    filesaver.save_content(
                        table_data, table_config["filename"]
                    )
