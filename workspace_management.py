import sqlite3
from datetime import datetime

class WorkspaceManagement:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path

    def connect_db(self):
        return sqlite3.connect(self.db_path)

    def create_workspace(self, name, slug, vectorTag=None, openAiTemp=None, openAiHistory=20, openAiPrompt=None):
        """Creates a new workspace."""
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO workspaces (name, slug, vectorTag, createdAt, lastUpdatedAt, openAiTemp, openAiHistory, openAiPrompt)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (name, slug, vectorTag, datetime.now(), datetime.now(), openAiTemp, openAiHistory, openAiPrompt))
            conn.commit()
            return f"Workspace '{name}' created successfully."
        except sqlite3.IntegrityError:
            return "Error: Workspace slug must be unique."
        finally:
            conn.close()

    def update_workspace(self, workspace_id, name=None, vectorTag=None, openAiTemp=None, openAiHistory=None, openAiPrompt=None):
        """Updates workspace details."""
        conn = self.connect_db()
        cursor = conn.cursor()
        updates = []
        params = []
        
        if name:
            updates.append("name = ?")
            params.append(name)
        if vectorTag:
            updates.append("vectorTag = ?")
            params.append(vectorTag)
        if openAiTemp is not None:
            updates.append("openAiTemp = ?")
            params.append(openAiTemp)
        if openAiHistory is not None:
            updates.append("openAiHistory = ?")
            params.append(openAiHistory)
        if openAiPrompt:
            updates.append("openAiPrompt = ?")
            params.append(openAiPrompt)
        
        params.append(datetime.now())  # Last updated timestamp
        params.append(workspace_id)

        if updates:
            query = f"UPDATE workspaces SET {', '.join(updates)}, lastUpdatedAt = ? WHERE id = ?"
            cursor.execute(query, tuple(params))
            conn.commit()

        conn.close()
        return f"Workspace ID '{workspace_id}' updated successfully."


    def upload_file_to_workspace(self, workspace_id, source_file_path):
        """Uploads a file into the workspace directory and saves metadata."""
        if not os.path.isfile(source_file_path):
            return "Error: Source file does not exist."

        # Create directory if it doesn't exist
        dest_folder = os.path.join("workspace_files", f"workspace_{workspace_id}")
        os.makedirs(dest_folder, exist_ok=True)

        # Copy file
        filename = os.path.basename(source_file_path)
        dest_path = os.path.join(dest_folder, filename)

        try:
            shutil.copy2(source_file_path, dest_path)
        except Exception as e:
            return f"Error copying file: {e}"

        # Insert metadata into database
        try:
            with self.connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO files (workspace_id, filename, filepath, uploadedAt)
                    VALUES (?, ?, ?, ?)
                """, (
                    workspace_id,
                    filename,
                    dest_path,
                    datetime.now().isoformat()
                ))
                conn.commit()
                return f"File '{filename}' uploaded successfully to workspace ID {workspace_id}."
        except Exception as e:
            return f"Error saving file metadata: {e}"

    def delete_workspace(self, workspace_id):
        """Deletes a workspace."""
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM workspaces WHERE id = ?", (workspace_id,))
        conn.commit()
        conn.close()
        return f"Workspace ID '{workspace_id}' deleted."
