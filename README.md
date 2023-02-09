# Bug showcase

https://github.com/codingjoe/django-select2/issues/203

In a fresh venv:
```console
$ pip install -r requirements.txt
...
$ # Individually lauching either test_1 or test_2 work
$ python manage.py test bugshowcase.tests.test_widget.TestShowcase.test_1
$ python manage.py test bugshowcase.tests.test_widget.TestShowcase.test2
$ # but luching the whole class fails
$ python manage.py test bugshowcase.tests.test_widget.TestShowcase
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.E
======================================================================
ERROR: test_2 (bugshowcase.tests.test_widget.TestShowcase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/joachim/other-src/select2_issue/bugshowcase/tests/test_widget.py", line 17, in test_2
    self.assertNotEqual(widget.render(name="foo", value="bar"), "")
  File "/home/joachim/.envs/select2_issue/lib/python3.10/site-packages/django/forms/widgets.py", line 246, in render
    context = self.get_context(name, value, attrs)
  File "/home/joachim/.envs/select2_issue/lib/python3.10/site-packages/django/forms/widgets.py", line 683, in get_context
    context = super().get_context(name, value, attrs)
  File "/home/joachim/.envs/select2_issue/lib/python3.10/site-packages/django/forms/widgets.py", line 643, in get_context
    context = super().get_context(name, value, attrs)
  File "/home/joachim/.envs/select2_issue/lib/python3.10/site-packages/django/forms/widgets.py", line 239, in get_context
    'attrs': self.build_attrs(self.attrs, attrs),
  File "/home/joachim/src/django-select2/django_select2/forms.py", line 99, in build_attrs
    "data-theme": self.theme or settings.SELECT2_THEME,
  File "/home/joachim/.envs/select2_issue/lib/python3.10/site-packages/django/conf/__init__.py", line 83, in __getattr__
    val = getattr(self._wrapped, name)
AttributeError: 'Settings' object has no attribute 'SELECT2_THEME'

----------------------------------------------------------------------
Ran 2 tests in 0.004s

FAILED (errors=1)
Destroying test database for alias 'default'...
```
