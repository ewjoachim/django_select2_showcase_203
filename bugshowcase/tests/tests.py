from django.test import TestCase, override_settings
from django.conf import settings

from unittest.mock import patch


class TestShowcase(TestCase):
    @override_settings(A=1)
    @patch("bugshowcase.select2.func", autospec=True)
    def test_1(self, s2):
        pass

    def test_2(self):
        assert settings.SELECT2_THEME
