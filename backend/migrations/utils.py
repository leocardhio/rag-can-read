def get_url(config) -> str:
    db_host = 'localhost'
    db_port = config.postgres_port
    db_user = config.postgres_user
    db_password = config.postgres_password
    db_name = config.postgres_db
    
    return f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"