import io
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

import sqlalchemy

from ...methods.extractors.databaseConnectors import (  # noqa: E501
    MySQLConnector,
    PostgresConnector,
)

mock_columns = ["COL1", "COL2", "COL3"]

mock_result = [
    ["col1-res1", "col2-res1", "col3-res1"],
    ["col1-res2", "col2-res2", "col3-res2"],
    ["col1-res3", "col2-res3", "col3-res3"],
]


class FakeQueryResult:
    def __init__(self):
        pass

    def keys(self):
        return mock_columns

    def all(self):
        return mock_result

    def fetchall(self):
        return self.all()


class MySQLConnectorTestSuite(TestCase):
    def setUp(self):
        self.user = "user"
        self.password = "password"
        self.host = "host"
        self.schema = "schema"
        self.port = "3306"
        sqlalchemy.create_engine = MagicMock()
        self.conn = MySQLConnector(
            self.user, self.password, self.host, self.port, self.schema
        )  # noqa: E501

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

    def test_can_query_data(self):
        self.conn.connect()
        self.conn._db_session.execute = MagicMock(
            return_value=FakeQueryResult()
        )
        result = self.conn.query_data("MY_TABLE")
        self.assertIsNotNone(result)

    def test_can_extract(self):
        self.conn.query_data = MagicMock(return_value=mock_result)
        data = self.conn.extract("MY_TABLE", columns=mock_columns)
        self.assertGreater(len(data), 0)

    def test_can_extract_and_return_other_format(self):
        self.conn.query_data = MagicMock(return_value=mock_result)
        data = self.conn.extract(
            "MY_TABLE", return_type="other", columns=mock_columns
        )
        self.assertEqual(len(data), 3)

    def test_can_create_connection_without_schema(self):
        self.conn = MySQLConnector(
            self.user, self.password, self.host, self.port
        )
        self.assertIsNone(self.conn._schema)


class PostgresConnectorTestSuite(TestCase):
    def setUpConnector(self):
        self.user = "user"
        self.password = "password"
        self.host = "host"
        self.port = "5432"
        self.db_name = "database"
        sqlalchemy.create_engine = MagicMock()
        self.conn = PostgresConnector(
            self.user, self.password, self.host, self.port, self.db_name
        )

    def captureStdout(self):
        stdout = io.StringIO()
        sys.stdout = stdout

        def restore():
            sys.stdout = sys.__stdout__

        return stdout, restore

    def setUp(self):
        self.setUpConnector()

    @patch("sqlalchemy.orm.sessionmaker")
    def test_can_connect(self, mock_sessionmaker):
        self.conn.connect()
        self.assertIsNotNone(self.conn._db_session)

    @patch(
        "sqlalchemy.orm.Session.__init__",
        side_effect=sqlalchemy.exc.OperationalError("error", [], None),
    )
    def test_can_connect_raises_OperationalError(self, mock_sessionmaker):
        stdout, restore = self.captureStdout()
        self.conn.connect()
        self.assertTrue("The following error occurred" in stdout.getvalue())
        restore()

    def test_can_disconnect(self):
        stdout, restore = self.captureStdout()
        self.conn.connect()
        self.conn.disconnect()
        self.assertTrue("Disconnected!" in stdout.getvalue())
        restore()

    def test_can_disconnect_does_nothing_if_already_disconnected(self):
        stdout, restore = self.captureStdout()
        self.conn.disconnect()
        self.assertTrue("Not connected to any database" in stdout.getvalue())
        restore()

    def test_can_sanitize_query(self):
        query = "SELECT * FROM MY_TABLE WHERE PARAM=SOME_VAL"
        sanitized = PostgresConnector.sanitize_query(query)
        self.assertEqual(query.lower(), str(sanitized))

    def test_can_sanitize_query_raises_exception_if_query_invalid(self):
        query = ";DROP TABLE WHERE 1=1;"
        with self.assertRaises(Exception):
            PostgresConnector.sanitize_query(query)

    def test_can_build_query_string(self):
        expected = "SELECT COL1,COL2 FROM MY_TABLE WHERE COL1 = COL2 LIMIT 10"
        query = PostgresConnector.build_query_string(
            "MY_TABLE", ["COL1", "COL2"], "COL1 = COL2", 10
        )
        self.assertEqual(query, expected)

    def test_can_build_query_string_handling_empty_values(self):
        expected = "SELECT * FROM MY_TABLE"
        query = PostgresConnector.build_query_string("MY_TABLE")
        self.assertEqual(query, expected)

    @patch("sqlalchemy.orm.Session.execute", return_value=FakeQueryResult())
    def test_can_query(self, mock_execute):
        self.conn.connect()
        data = self.conn.query_data("MY_TABLE")
        self.assertEqual(len(data), 3)

    def test_can_query_raises_OperationalError(self):
        stdout, restore = self.captureStdout()
        self.conn.connect()
        self.conn.query_data("MY_TABLE")
        self.assertTrue("Error executing query" in stdout.getvalue())
        restore()

    def test_can_query_returns_nothing_if_no_session(self):
        data = self.conn.query_data("MY_TABLE")
        self.assertIsNone(data)

    def test_can_extract(self):
        self.conn.query_data = MagicMock(return_value=mock_result)
        data = self.conn.extract("MY_TABLE", columns=mock_columns)
        self.assertGreater(len(data), 0)

    def test_can_extract_and_return_other_format(self):
        self.conn.query_data = MagicMock(return_value=mock_result)
        data = self.conn.extract(
            "MY_TABLE", return_type="other", columns=mock_columns
        )
        self.assertEqual(len(data), 3)
