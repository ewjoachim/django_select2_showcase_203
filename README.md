# Bug showcase

In a fresh venv:
```console
$ pip install -r requirements.txt
...
$ python manage.py test bugshowcase/tests
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.E
======================================================================
ERROR: test_2 (tests.TestShowcase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/joachim/other-src/select2_issue/bugshowcase/tests/tests.py", line 14, in test_2
    assert settings.SELECT2_THEME
  File "/home/joachim/.envs/select2_issue/lib/python3.10/site-packages/django/conf/__init__.py", line 83, in __getattr__
    val = getattr(self._wrapped, name)
AttributeError: 'Settings' object has no attribute 'SELECT2_THEME'

----------------------------------------------------------------------
Ran 2 tests in 0.003s

FAILED (errors=1)
Destroying test database for alias 'default'...

```
