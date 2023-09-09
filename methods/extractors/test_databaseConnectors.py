from unittest import TestCase
from unittest.mock import MagicMock

import sqlalchemy

from .databaseConnectors import MySQLConnector


class FakeQueryResult:
    def __init__(self):
        pass

    def keys(self):
        return ["COL1", "COL2", "COL3"]

    def all(self):
        return [
            ["col1-res1", "col2-res1", "col3-res1"],
            ["col1-res2", "col2-res2", "col3-res2"],
            ["col1-res3", "col2-res3", "col3-res3"],
        ]


class MySQLConnectorTestSuite(TestCase):
    def setUp(self):
        self.user = "user"
        self.password = "password"
        self.host = "host"
        self.schema = "schema"
        sqlalchemy.create_engine = MagicMock()
        self.conn = MySQLConnector(self.user, self.password,
                                   self.host, self.schema)

    def test_can_sanitize_query(self):
        query = "SELECT * FROM MY_TABLE WHERE PARAM=SOME_VAL"
        sanitized = MySQLConnector.sanitize_query(query)
        self.assertEqual(query.lower(), sanitized)

    def test_can_sanitize_query_raises_exception_if_query_invalid(self):
        query = ";DROP TABLE WHERE 1=1;"
        with self.assertRaises(Exception):
            MySQLConnector.sanitize_query(query)

    def test_can_build_query_string(self):
        expected = "SELECT COL1,COL2 FROM MY_TABLE WHERE COL1 = COL2 LIMIT 10"
        query = MySQLConnector.build_query_string(
            "MY_TABLE", ["COL1", "COL2"], "COL1 = COL2", 10
        )
        self.assertEqual(query, expected)

    def test_can_build_query_string_handling_empty_values(self):
        expected = "SELECT * FROM MY_TABLE"
        query = MySQLConnector.build_query_string("MY_TABLE")
        self.assertEqual(query, expected)

    def test_can_query(self):
        # TODO: find better way to test this, (no 'assert no raises')
        self.conn.query("MY_TABLE")

    def test_can_extract(self):
        self.conn.query = MagicMock(return_value=FakeQueryResult())
        data = self.conn.extract("MY_TABLE")
        self.assertGreater(len(data), 0)

    def test_can_extract_and_return_other_format(self):
        self.conn.query = MagicMock(return_value=FakeQueryResult())
        data = self.conn.extract("MY_TABLE", return_type="other")
        self.assertEqual(len(data), 3)

    def test_can_create_connection_without_schema(self):
        self.conn = MySQLConnector(self.user, self.password, self.host)
        self.assertIsNone(self.conn._schema)
