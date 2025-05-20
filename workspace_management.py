import requests
import os

class WorkspaceAPI:
    def __init__(self, base_url="https://linbeckai.com/", api_key=None):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

    def create_workspace(self, name, slug):
        url = f"{self.base_url}/v1/workspace/new"
        payload = {"name": name, "slug": slug}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def update_workspace(self, slug, **kwargs):
        url = f"{self.base_url}/v1/workspace/{slug}/update"
        payload = {k: v for k, v in kwargs.items() if v is not None}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def upload_file_to_workspace(self, slug, file_path):
        url = f"{self.base_url}/v1/document/upload"
        if not os.path.isfile(file_path):
            return {"error": "File does not exist."}
        files = {"file": open(file_path, "rb")}
        data = {"workspace": slug}
        response = requests.post(url, headers=self.headers, files=files, data=data)
        return response.json()

    def delete_workspace(self, slug):
        url = f"{self.base_url}/v1/workspace/{slug}"
        response = requests.delete(url, headers=self.headers)
        return response.json()

    def list_workspaces(self):
        url = f"{self.base_url}/v1/workspaces"
        response = requests.get(url, headers=self.headers)
        return response.json()
