class UserManagement:
    def __init__(self, api_key: str | None = None,
                 base_url: str = "https://linbeckai.com"):
        self.base = base_url.rstrip("/")
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

   def add_user(self, email, password, role="default"):
        url = f"{self.base}/v1/admin/users/new"
        payload = {"email": email, "password": password, "role": role}
        return requests.post(url, json=payload, headers=self.headers).json()

   def delete_user(self, user_id):
        url = f"{self.base}/v1/admin/users/{user_id}"
        return requests.delete(url, headers=self.headers).json()

  def assign_users(self, workspace_id: int, user_ids: list[int],
                     role: str = "member"):
        url = f"{self.base}/v1/admin/workspaces/{workspace_id}/update-users"
        payload = {"users": user_ids, "role": role}
        return requests.post(url, json=payload, headers=self.headers).json()


##ip of instance pass ssh in database, provision, instal to anl anything llm library, make changes to app, create users, provide access
#change it given anything llm, write code to run instance on its own, start thinking about that code, unit tests,
