django-admin-email-sender
=======================

This package used to send mass emails from Admin Panel.

Installation
============

First install the module, preferably in a virtual environment::

`pip install django-admin-email-sender`

Or install the current repository::

`pip install -e git+https://github.com/stasfilin/django-admin-email-sender.git#egg=django-admin-email-sender`


Configuration
-------------

Next, create a project which uses the application::
```bash
cd ..
django-admin.py startproject demo-project
```

Add the following to ``settings.py``:

```python

INSTALLED_APPS += (
    'admin_email_sender',
)
```


Issues
------

Use the GitHub `Issues` for django-admin-email-sender to submit bugs, issues, and feature requests.

Todo
----

- [ ] Email Templates Support
- [ ] Async emails
- [ ] Scheduled emails


Contributing
------------

Pull requests are welcome. :-)

