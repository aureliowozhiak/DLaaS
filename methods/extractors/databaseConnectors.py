import sqlalchemy
import json

class MySQLConnector:
    def __init__(self, user:str, password:str, host:str, schema:str):
        self._user = user
        self._password = password
        self._host = host
        self._schema = schema
        self._engine = self._set_engine()
        self._connection = self._engine.connect()

    def _set_engine(self):
        if self._schema is None:
            connection_string = f"mysql+pymysql://{self._user}:{self._password}@{self._host}"
        else:
            connection_string = f"mysql+pymysql://{self._user}:{self._password}@{self._host}/{self._schema}"
        return sqlalchemy.create_engine(connection_string, pool_recycle=3600)

    def sanitize_query(query:str):
        #TODO: Melhorar a fumção de sanitização para evitar SQL injections
        query = query.lower().strip()
        query = query.replace("--", "")
        query = query.split(";")[0]
        if query.startswith("select") and "from" in query:
            return query
        else:
            raise Exception("Invalid query")

    def build_query_string(table:str, columns:list = None, where:str = None, limit:int = None):
        if columns is None or columns == []:
            select_columns = "*"
        else:
            select_columns = ",".join(columns)
        query_string = f"SELECT {select_columns} FROM {table}"
        if not (where is None):
            query_string += f" WHERE {where}"
        if not (limit is None):
            query_string += f" LIMIT {limit}"
        return query_string

    def query(self, table:str, columns:list = None, where:str = None, limit:int = None):
        query = MySQLConnector.build_query_string(table, columns, where, limit)
        with self._connection as conn:
            return conn.execute(sqlalchemy.text(query))

    def extract(self, table:str, columns:list = None, where:str = None, limit = None):
        result = self.query(table, columns, where, limit)
        columns = [col for col in result.keys()]
        data = []
        for row in result.all():
            row_data = {}
            for value in zip(columns, row):
                row_data[value[0]] = value[1]
            data.append(row_data)
        return json.dumps(data, ensure_ascii=False)
