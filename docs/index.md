---
hide:
  - navigation
---

# GOV.UK Frontend Django

The `govuk_frontend_django` package contains django functionality to help when building a GOV.UK website.

The main part of this package is the [template tags](./template-tags/index.md) that it offers for use in your templates. These template tags will reduce the amount of markup that you need to maintain in your project.

This package also contains some helpful [templates](./templates/index.md) for your project, such as the `govuk_frontend_django/base.html` template which contains the basic structure of a GOV.UK website.

## Getting started

First install the package:
```bash
pip install govuk-frontend-django

# or

poetry add govuk-frontend-django
```

In your settings file, add the app to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    "govuk_frontend_django",
]
```