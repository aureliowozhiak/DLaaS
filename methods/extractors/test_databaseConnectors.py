from unittest import TestCase
from unittest.mock import MagicMock

from .databaseConnectors import MySQLConnector


class MySQLConnectorTestSuite(TestCase):
    def setUp(self):
        self.user = "user"
        self.password = "password"
        self.host = "host"
        self.schema = "schema"
        MySQLConnector._set_engine = MagicMock()
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
        query = MySQLConnector.build_query_string("MY_TABLE", ["COL1", "COL2"],
                                                  "COL1 = COL2", 10)
        self.assertEqual(query, expected)

    def test_can_build_query_string_handling_empty_values(self):
        expected = "SELECT * FROM MY_TABLE"
        query = MySQLConnector.build_query_string("MY_TABLE")
        self.assertEqual(query, expected)
