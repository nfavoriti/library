import sqlite3
from datetime import datetime

class UserManagement:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path

    def connect_db(self):
        return sqlite3.connect(self.db_path)

    def add_user(self, username, password, role='default'):
        """Adds a new user to the system."""
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO users (username, password, role, createdAt, lastUpdatedAt)
                VALUES (?, ?, ?, ?, ?)
            """, (username, password, role, datetime.now(), datetime.now()))
            conn.commit()
            return f"User '{username}' added successfully."
        except sqlite3.IntegrityError:
            return "Error: Username already exists."
        finally:
            conn.close()

    def delete_user(self, user_id):
        """Deletes a user and their associated workspaces."""
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
        return f"User ID '{user_id}' deleted."

    def assign_user_to_workspace(self, user_id, workspace_id, role):
        """Assigns a user to a workspace."""
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO user_workspaces (user_id, workspace_id, role)
                VALUES (?, ?, ?)
            """, (user_id, workspace_id, role))
            conn.commit()
            return f"User ID '{user_id}' assigned to workspace '{workspace_id}' as '{role}'."
        except sqlite3.IntegrityError:
            return "Error: User is already assigned to this workspace."
        finally:
            conn.close()


##ip of instance pass ssh in database, provision, instal to anl anything llm library, make changes to app, create users, provide access
#change it given anything llm, write code to run instance on its own, start thinking about that code, unit tests,
