from library.config import get_db_connction
from library.generate_api import generate_api_key

def store_api_key(created_by_user_id=None):
    """Generates and stores a new API key in the database."""
    conn = get_db_connction()
    cursor = conn.cursor()

    try:
        new_api_key = generate_api_key()
        print("generated new api key")

        cursor.execute(
            "INSERT INTO api_keys (secret, createdBy) VALUES (?, ?)",
            (new_api_key, created_by_user_id),
        )
        conn.commit()

        print(f"API Key Stored: {new_api_key}")
        return new_api_key

    except Exception as e:
        print(f"Error storing API key: {e}")
        return None

    finally:
        conn.close()

if __name__ == "__main__":
    store_api_key()