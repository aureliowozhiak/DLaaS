import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import json


class MySQLConnector:
    def __init__(self, user: str, password: str, host: str, schema: str):
        self._user = user
        self._password = password
        self._host = host
        self._schema = schema
        self._engine = self._set_engine()
        self._connection = self._engine.connect()

    def _set_engine(self):
        if self._schema is None:
            connection_string = ''.join(
                f"mysql+pymysql://{self._user}:{self._password}@", self._host)
        else:
            connection_string = ''.join(
                f"mysql+pymysql://{self._user}:{self._password}@",
                f"{self._host}/{self._schema}")
        return sqlalchemy.create_engine(connection_string, pool_recycle=3600)

    def sanitize_query(query: str):
        # TODO: Melhorar a fumção de sanitização para evitar SQL injections
        query = query.lower().strip()
        query = query.replace("--", "")
        query = query.split(";")[0]
        if query.startswith("select") and "from" in query:
            return query
        else:
            raise Exception("Invalid query")

    def build_query_string(table: str, columns: list = None, where: str = None,
                           limit: int = None):
        if columns is None or columns == []:
            select_columns = "*"
        else:
            select_columns = ",".join(columns)
        query_string = f"SELECT {select_columns} FROM {table}"
        if where is not None:
            query_string += f" WHERE {where}"
        if limit is not None:
            query_string += f" LIMIT {limit}"
        return query_string

    def query(self, table: str, columns: list = None, where: str = None,
              limit: int = None):
        query = MySQLConnector.build_query_string(table, columns, where, limit)
        with self._connection as conn:
            return conn.execute(sqlalchemy.text(query))

    def extract(self, table: str, columns: list = None, where: str = None,
                limit: int = None, return_type: str = "json"):
        result = self.query(table, columns, where, limit)
        columns = [col for col in result.keys()]
        data = []
        for row in result.all():
            row_data = {}
            for value in zip(columns, row):
                row_data[value[0]] = value[1]
            data.append(row_data)
        if return_type == "json":
            return json.dumps(data, ensure_ascii=False)
        else:
            return data


class PostgresConnector:
    def __init__(self, user: str, password: str, host: str, port: str,
                 db_name: str) -> None:
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._db_name = db_name
        self._connection_string = ''.join(
            f'postgresql://{self._user}:{self._password}@',
            f'{self._host}:{self._port}/{self._db_name}')
        self._engine = create_engine(self._connection_string)
        self._db_session = None

    def connect(self):
        try:
            Session = sessionmaker(bind=self._engine)
            self._db_session = Session()
            print('Successfully connected!')
        except OperationalError as e:
            print(f'The following error occurred: {e}')

    def disconnect(self):
        if self._db_session:
            self._db_session.close()
            print('Disconnected!')
        else:
            print('Not connected to any database')

    # Função criada pelo devbrunorm
    def sanitize_query(query: str):
        query = query.lower().strip()
        query = query.replace("--", "")
        query = query.split(";")[0]
        if query.startswith("select") and "from" in query:
            return text(query)
        else:
            raise Exception("Invalid query")

    # Função criada pelo devbrunorm
    def build_query_string(table: str, columns: list = None, where: str = None,
                           limit: int = None):
        if columns is None or columns == []:
            select_columns = "*"
        else:
            select_columns = ",".join(columns)
        query_string = f"SELECT {select_columns} FROM {table}"
        if where is not None:
            query_string += f" WHERE {where}"
        if limit is not None:
            query_string += f" LIMIT {limit}"
        return query_string

    def query_data(self, table: str, columns: list = None, where: str = None,
                   limit: int = None):
        query = PostgresConnector.build_query_string(table, columns, where,
                                                     limit)
        if self._db_session:
            try:
                data = self._db_session.execute(text(query)).fetchall()
                return data
            except OperationalError as e:
                print(f'Error executing query: {e}')

    # Função criada pelo devbrunorm
    def extract(self, table: str, columns: list = None, where: str = None,
                limit: int = None, return_type: str = "json"):
        result = self.query_data(table, columns, where, limit)
        columns = [col for col in result.keys()]
        data = []
        for row in result.all():
            row_data = {}
            for value in zip(columns, row):
                row_data[value[0]] = value[1]
            data.append(row_data)
        if return_type == "json":
            return json.dumps(data, ensure_ascii=False)
        else:
            return data
