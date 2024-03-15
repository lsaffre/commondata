from unittest import TestCase
import doctest


class DocTests(TestCase):

    def test_docs(self):
        # doctest.testfile("../README.rst", encoding="utf-8", raise_on_error=True)
        (failures, tests) = doctest.testfile("../README.rst", encoding="utf-8")
        self.assertEqual(failures, 0)
