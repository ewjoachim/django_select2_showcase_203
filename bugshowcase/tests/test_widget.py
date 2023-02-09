from django.test import TestCase, override_settings
from django.conf import settings

from unittest.mock import patch


class TestShowcase(TestCase):
    @override_settings(USE_I18N=False)
    @patch("bugshowcase.select2.get_widget", autospec=True)
    def test_1(self, s2):
        self.assertEqual(1 + 1, 2)

    def test_2(self):
        from bugshowcase.select2 import get_widget

        widget = get_widget()
        self.assertNotEqual(widget.render(name="foo", value="bar"), "")
