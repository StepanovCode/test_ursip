import os

from dotenv import load_dotenv

load_dotenv()

dsn = {
    'dbname': "ursip_db",
    'user': os.environ.get("POSTGRES_USER"),
    'password': os.environ.get("POSTGRES_PASSWORD"),
    'host': "localhost",
    'port': "8080",
}
