class Settings():
    PROJECT_TITLE: str = 'Bookstore RestAPI'
    PROJECT_VERSION: str = '0.1.0'

    # postgres settings

    POSTGRES_LOCAL: bool = False
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str = '5432' # Default Port for postgreSQL
    POSTGRES_DB: str
    # BEFORE CHANGING ANYTHING HERE ... READ CAREFULLY
    # If (POSTGRES_LOCAL = True) it will use your local postgreSQL db
    # Set to False to use the one made on heroku
    if POSTGRES_LOCAL:
        # Change settings for your local db
        POSTGRES_USER = 'meta'
        POSTGRES_PASSWORD = ''
        POSTGRES_SERVER = 'localhost'
        POSTGRES_DB = 'bookstore_db'
    else:
        # DO NOT CHANGE THIS SETTINGS
        POSTGRES_USER = 'bdxhjdcqyfiqgn'
        POSTGRES_PASSWORD = 'fd0d26d9c399001fededf933b682b043693fbac1ac0c62fa9104e7cc35e72f2b'
        POSTGRES_SERVER = 'ec2-52-86-177-34.compute-1.amazonaws.com'
        POSTGRES_DB = 'd5ajmo38v0i5q8'

    POSTGRES_URL: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'
    print(f'Using: {POSTGRES_URL}')
settings = Settings()