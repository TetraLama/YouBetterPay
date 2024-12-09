import os

class Config:
    mongo_db_name = os.getenv('MONGO_DB_NAME', 'youbetterpay')
    mongo_db_user = os.getenv('MONGO_DB_USER', 'youbetterpay')
    mongo_db_password = os.getenv('MONGO_DB_PASSWORD', 'MySup3rS3cur3P@ssw0rd!')
    mongo_db_host = os.getenv('MONGO_DB_HOST', 'db')
    mongo_db_port = os.getenv('MONGO_DB_PORT', 27017)
    mongo_uri = f"mongodb://{mongo_db_user}:{mongo_db_password}@{mongo_db_host}:{mongo_db_port}/{mongo_db_name}?authSource=admin"