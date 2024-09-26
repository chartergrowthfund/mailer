# mailer


## Setup
Expects a secret in Google Secret manager called: `MAILGUN_TOKEN`. 

TODO: add an option to pull the token from environment as well.


## Example Usages:

### Sending a simple message

```python
from mailer import Mailer


email = Mailer()
email.recipients = ["recipient1@example.com", "recipient2@example.com"]
email.subject = "This is the subject line"

email.send_message("This is a test message")
```

### Sending a custom HTML message

```python
from mailer import Mailer


email = Mailer()
email.recipients = ["recipient1@example.com", "recipient2@example.com"]
email.subject = "This is the subject line"

html = """
<html>
  <p> Dear Recipient,</p>
  <br>
  <p>This is a <strong>very important</strong> message.</p>
</html>
"""

email.send_html(html)
```

### Sending from a Mailgun template

```python
from mailer import Mailer


email = Mailer()
email.recipients = ["recipient1@example.com", "recipient2@example.com"]
email.cc = ["additional_cc@example.com"]
email.subject = "This is the subject line"
email.template = "mailgun_template_name"

email.template_vars = {
    "template_var1": "value1",
    "template_var2": "value2",
}
email.send_template()
```

### Attaching files

```python
from mailer import Mailer


email = Mailer()
email.recipients = ["recipient1@example.com", "recipient2@example.com"]
email.subject = "This is the subject line"
email.files(filepaths=["path_to_file/file_name.pdf"])

email.send_message("This is a test message")
```