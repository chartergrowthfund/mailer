from setuptools import setup
from os import path


setup(
    name="mailer",
    version="0.0.1",
    description="Utility module for sending bulk emails via Mailgun API",
    long_description="Utility module for sending bulk emails via Mailgun API",
    url="https://github.com/chartergrowthfund/mailer",
    author="dchess",
    author_email="dc.hess@gmail.com",
    packages=["mailer"],
    install_requires=[
        "requests", 
        "google-cloud-secret-manager"
    ],
    zip_safe=False,
)