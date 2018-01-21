from django.test import TestCase

from admin_email_sender.helpers import DEFAULT_HTML
from admin_email_sender.validators import validate_tags


class TagsValidatorTest(TestCase):

    def test_with_valid_data(self):
        status = validate_tags(DEFAULT_HTML)

        assert status is None

    def test_with_invalid_data(self):
        with self.assertRaises(Exception) as context:
            validate_tags('<p>Hey</p>')

        self.assertTrue('I can find @body tag' in context.exception)
