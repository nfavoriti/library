import sqlite3
import os
from datetime import datetime

class DataManagement:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path

    def connect_db(self):
        return sqlite3.connect(self.db_path)

    def upload_file(self, docId, filename, docpath, workspaceId, metadata=None):
        """Uploads a document to a workspace."""
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO workspace_documents (docId, filename, docpath, workspaceId, metadata, createdAt, lastUpdatedAt)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (docId, filename, docpath, workspaceId, metadata, datetime.now(), datetime.now()))
            conn.commit()
            return f"File '{filename}' uploaded successfully."
        except sqlite3.IntegrityError:
            return "Error: Duplicate docId. Choose a unique identifier."
        finally:
            conn.close()

    def get_files_by_workspace(self, workspaceId):
        """Retrieves all files for a given workspace."""
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM workspace_documents WHERE workspaceId = ?", (workspaceId,))
        files = cursor.fetchall()
        conn.close()
        return files

    def delete_file(self, docId):
        """Deletes a file based on its document ID."""
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM workspace_documents WHERE docId = ?", (docId,))
        conn.commit()
        conn.close()
        return f"File with docId '{docId}' deleted."
