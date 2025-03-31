import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

# Construct the correct absolute path to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = os.getenv("DATABASE_URL", os.path.join(BASE_DIR, "../server/storage/anythingllm.db"))

def get_db_connction():
    if not os.path.exists(DATABASE_URL):
        raise FileNotFoundError(f"Database file not found at {DATABASE_URL}")

    connection = sqlite3.connect(DATABASE_URL)
    connection.row_factory = sqlite3.Row
    return connection
