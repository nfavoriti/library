from library.config import get_db_connction

def get_api_key():
    connection = get_db_connction()
    cursor = connection.cursor()


    try:
        cursor.execute("SELECT secret FROM api_keys ORDER BY createdAt DESC LIMIT 1")
        api_key = cursor.fetchone()

        if api_key:
            return api_key["secret"]
        
        else:
            return None
    except Exception as e:
        print({e})
        return None
    finally:
        connection.close()
