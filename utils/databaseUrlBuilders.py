def build_mysql_url(
    user: str, password: str, port: str, host: str, schema: str = None
) -> str:
    if schema is None:
        return f"mysql+pymysql://{user}:{password}@{host}:{port}"  # noqa: E501
    else:
        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema}"  # noqa: E501


def build_postgres_url(
    user: str, password: str, host: str, port: str, db_name: str
) -> str:
    return (
        f"postgresql://{user}:{password}@{host}:{port}/{db_name}"  # noqa: E501
    )


def build_sqlite_url(db_path: str) -> str:
    return f"sqlite:///{db_path}"
