import json
import logging
import os

from methods.extractors.apiRequests import ApiRequests
from methods.extractors.databaseConnectors import MySQLConnector
from methods.extractors.webPageDataScrappers import WebPageDataScrappers
from methods.loaders.fileSavers import FileSavers

# Configurar o sistema de log
log_file = "logs/init.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
)

config_path = "config_files"
filesaver = FileSavers()

for filename in os.listdir(config_path):
    full_path = os.path.join(config_path, filename)
    if os.path.isfile(full_path):
        logging.info(f"Processando arquivo de configuração: {filename}")
        with open(full_path, "r") as file:
            config_file = json.load(file)

        for url, v in config_file.items():
            if "webscrapper" in filename:
                logging.info(f"Executando web scraping para a URL: {url}")
                webscrapper = WebPageDataScrappers(url)
                for i in v:
                    filesaver.save_content(
                        webscrapper.handle_content(i["tag"], i["attrs"]),
                        i["file_name"],
                        i["attrs"],
                        sep=i["sep"],
                    )

            if "api" in filename:
                logging.info(f"Fazendo solicitação API para a URL: {url}")
                for i in v:
                    response = json.dumps(
                        ApiRequests(url, headers=i["api_headers"])
                        .make_request(i["endpoint_path"])
                        .json()
                    )
                    filesaver.save_content(response, i["file_name"])

            if "mysql" in filename:
                logging.info(f"Conectando ao banco de dados host={url}")
                host = url
                port = v["port"]
                user = v["user"]
                password = v["password"]
                db_name = v.get("db_name")  # opcional
                connector = MySQLConnector(
                    user=user,
                    password=password,
                    host=host,
                    port=port,
                    schema=db_name,
                )
                connector.connect()
                for table, table_config in v["tables"].items():
                    table_data = connector.extract(
                        table,
                        table_config.get("columns"),
                        table_config.get("where"),
                        table_config.get("limit"),
                    )
                    filesaver.save_content(table_data, table_config["filename"])

# Feche o arquivo de log após o término do programa
logging.shutdown()
