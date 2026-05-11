def get_url(config, **kwargs) -> str:
    db_host = 'localhost'
    db_port = config.postgres_port
    db_user = config.postgres_user
    db_password = config.postgres_password
    db_name = config.postgres_db

    with_driver = kwargs.get('with_driver', True)
    if with_driver:
        return f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"