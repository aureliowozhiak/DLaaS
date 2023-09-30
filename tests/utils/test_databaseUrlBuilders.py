from unittest import TestCase

from ...src.utils.databaseUrlBuilders import (
    build_mysql_url,
    build_postgres_url,
    build_sqlite_url,
)


class TestBuildMysqlUrl(TestCase):
    def test_build_mysql_url_schema_none(self):
        result = build_mysql_url("user", "password", "3306", "localhost")
        self.assertEqual(
            result, "mysql+pymysql://user:password@localhost:3306"
        )

    def test_build_mysql_url_schema_not_none(self):
        result = build_mysql_url(
            "user", "password", "3306", "localhost", "mydb"
        )
        self.assertEqual(
            result, "mysql+pymysql://user:password@localhost:3306/mydb"
        )


class TestBuildPostgresUrl(TestCase):
    def test_build_postgres_url(self):
        self.assertEqual(
            build_postgres_url("user", "pass", "localhost", "5432", "my_db"),
            "postgresql://user:pass@localhost:5432/my_db",
        )

    def test_build_postgres_url_empty(self):
        self.assertEqual(
            build_postgres_url("", "", "", "", ""), "postgresql://:@:/"
        )


class TestBuildSqliteUrl(TestCase):
    def test_build_sqlite_url_valid_path(self):
        db_path = "path/to/database.db"
        expected_url = "sqlite:///path/to/database.db"
        self.assertEqual(build_sqlite_url(db_path), expected_url)

    def test_build_sqlite_url_empty_path(self):
        db_path = ""
        expected_url = "sqlite:///"
        self.assertEqual(build_sqlite_url(db_path), expected_url)
