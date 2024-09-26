import requests
from mailer.secret_manager import Secret
import json
from pathlib import Path


class Mailer:
    def __init__(self, sender=None):
        self.url = "https://api.mailgun.net/v3/mg.chartergrowthfund.org/messages"
        self.secrets = Secret()
        self.token = self.secrets.access("MAILGUN_TOKEN")
        self.auth = ("api", self.token)
        self.sender = sender
        self.subject = None
        self.template = None
        self.recipients = []
        self.cc = []
        self._files = []
        self._template_vars = None

    @property
    def template_vars(self):
        return self._template_vars

    @template_vars.setter
    def template_vars(self, variables):
        self._template_vars = json.dumps(variables)

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, filepaths=[]):
        self._files = []
        for filepath in filepaths:
            filename = Path(filepath).name
            attachment = ("attachment", (filename, open(filepath, "rb").read()))
            self._files.append(attachment)

    def send_template(self):
        data = {
            "from": self.sender,
            "to": self.recipients,
            "cc": self.cc,
            "subject": self.subject,
            "template": self.template,
        }
        files = self.files or None
        if self.template_vars:
            data["h:X-Mailgun-Variables"] = self.template_vars
        return requests.post(self.url, auth=self.auth, data=data, files=files)

    def send_message(self, text):
        data = {
            "from": self.sender,
            "to": self.recipients,
            "subject": self.subject,
            "text": text,
        }
        return requests.post(self.url, auth=self.auth, data=data)

    def send_html(self, html):
        data = {
            "from": self.sender,
            "to": self.recipients,
            "subject": self.subject,
            "html": html,
        }
        return requests.post(self.url, auth=self.auth, data=data)