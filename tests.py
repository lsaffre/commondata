from unittest import TestCase
import doctest


class DocTests(TestCase):

    def test_docs(self):
        doctest.testfile("README.rst", encoding="utf-8")
