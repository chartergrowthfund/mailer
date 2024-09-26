from google.cloud import secretmanager


class Secret:
    def __init__(self):
        self.client = secretmanager.SecretManagerServiceClient()
        credentials = self.client._transport._credentials.__dict__
        self.project_id = credentials.get("_project_id") or credentials.get("_quota_project_id")

    def access(self, secret_id):
        """
        Return the value of a managed secret
        """
        name = f"projects/{self.project_id}/secrets/{secret_id}/versions/latest"
        response = self.client.access_secret_version(request={"name": name})

        # Decode secret payload from bytes to string.
        payload = response.payload.data.decode("UTF-8")
        return payload

    def update(self, secret_id, payload):
        """
        Add a new secret version to the given secret with the provided payload.
        """
        parent = self.client.secret_path(self.project_id, secret_id)

        # Convert the string payload into a bytes.
        payload = payload.encode("UTF-8")

        # Add the secret version.
        request = {"parent": parent, "payload": {"data": payload}}
        response = self.client.add_secret_version(request=request)
        return response
